import logging
import os
import sys
from contextlib import asynccontextmanager
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:     %(name)s - %(message)s",
    stream=sys.stdout,
)

_backend_dir = Path(__file__).parent
_project_root = _backend_dir.parent
for _p in [str(_project_root), str(_backend_dir / "apps")]:
    if _p not in sys.path:
        sys.path.insert(0, _p)

import httpx  # noqa: E402
from dotenv import load_dotenv  # noqa: E402
from fastapi import Depends, FastAPI, Request, Response  # noqa: E402
from fastapi.responses import JSONResponse  # noqa: E402
from fastapi.middleware.cors import CORSMiddleware  # noqa: E402
from pydantic import BaseModel  # noqa: E402
from sqlalchemy import text  # noqa: E402
from sqlalchemy.ext.asyncio import AsyncSession  # noqa: E402
import json  # noqa: E402
from backend.core.database import Base, get_db, engine  # noqa: E402
from backend.apps.titanic.domain.entities.titanic_entity import TitanicPassenger  # noqa: E402, F401
from backend.apps.friday13th.domain.entities.user_entity import UserModel  # noqa: E402, F401
from matrix.app.keymaker import get_keymaker, GEMINI_MODEL  # noqa: E402
from backend.apps.friday13th.adapter.inbound.api.v1.login_command_router import login_command_router  # noqa: E402
from backend.apps.friday13th.adapter.inbound.api.v1.signup_command_router import signup_command_router  # noqa: E402
from backend.apps.friday13th.adapter.inbound.api.v1.signup_query_router import signup_query_router  # noqa: E402
from backend.apps.friday13th.app.use_cases.login_command_interactor import LoginCommandInteractor  # noqa: E402
from backend.apps.friday13th.adapter.outbound.pg.login_command_pg_repository import LoginCommandPgRepository  # noqa: E402
from backend.apps.friday13th.app.use_cases.signup_command_interactor import SignupCommandInteractor  # noqa: E402
from backend.apps.friday13th.adapter.outbound.pg.signup_command_pg_repository import SignupCommandPgRepository  # noqa: E402
from backend.apps.friday13th.app.use_cases.signup_query_interactor import SignupQueryInteractor  # noqa: E402
from backend.apps.friday13th.adapter.outbound.pg.signup_query_pg_repository import SignupQueryPgRepository  # noqa: E402
from backend.apps.titanic.adapter.inbound.api import titanic_router  # noqa: E402
from backend.apps.titanic.app.use_cases.passenger_query_interactor import PassengerQueryInteractor  # noqa: E402
from backend.apps.titanic.adapter.outbound.pg.passenger_query_pg_repository import PassengerQueryPgRepository  # noqa: E402
from backend.apps.titanic.app.use_cases.train_interactor import JackService  # noqa: E402
from backend.apps.titanic.app.use_cases.james_command_interactor import JamesCommandInteractor  # noqa: E402
from backend.apps.titanic.adapter.outbound.pg.james_command_pg_repository import JamesCommandPgRepository  # noqa: E402
from backend.apps.titanic.app.use_cases.walter_query_interactor import WalterQueryInteractor  # noqa: E402
from backend.apps.titanic.adapter.outbound.pg.walter_query_pg_repository import WalterQueryPgRepository  # noqa: E402

logger = logging.getLogger("uvicorn.error")

load_dotenv(Path(__file__).parents[1] / ".env")


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    app.state.jack = await JackService.create()
    app.state.james = JamesCommandInteractor(JamesCommandPgRepository())
    app.state.walter_query = WalterQueryInteractor(WalterQueryPgRepository())
    app.state.passenger_query_interactor = PassengerQueryInteractor(PassengerQueryPgRepository())
    app.state.login_interactor = LoginCommandInteractor(LoginCommandPgRepository())
    app.state.signup_interactor = SignupCommandInteractor(SignupCommandPgRepository())
    app.state.signup_query_interactor = SignupQueryInteractor(SignupQueryPgRepository())
    yield


app = FastAPI(title="Main page", lifespan=lifespan)

CORS_ORIGINS = ["http://localhost:3000", "http://localhost:8000", "http://127.0.0.1:3000", "http://127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(titanic_router)
app.include_router(login_command_router)
app.include_router(signup_query_router)
app.include_router(signup_command_router)


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.exception("처리되지 않은 예외 발생 — %s %s", request.method, request.url)
    response = JSONResponse(status_code=500, content={"detail": str(exc)})
    origin = request.headers.get("origin")
    if origin in CORS_ORIGINS:
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

keymaker = get_keymaker()


@app.get("/")
def read_root():
    content = {"message": "FAST API 메인 페이지", "docs": "/docs"}
    json_str = json.dumps(content, ensure_ascii=False, indent=4)
    return Response(content=json_str.encode("utf-8"), media_type="application/json; charset=utf-8")

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat(req: ChatRequest):
    if keymaker.client is None:
        return {"error": "Gemini API key가 설정되지 않았습니다."}
    try:
        response = keymaker.client.models.generate_content(model=GEMINI_MODEL, contents=req.message)
        return {"reply": response.text}
    except Exception as e:
        return {"error": str(e)}


@app.get("/weather")
async def get_weather(lat: float, lon: float):
    api_key = os.getenv("OPENWEATHER_API_KEY", "")
    if not api_key:
        return {"error": "OpenWeather API key가 설정되지 않았습니다."}
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={"lat": lat, "lon": lon, "appid": api_key, "units": "metric", "lang": "kr"},
            )
            data = res.json()
        return {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
            "humidity": data["main"]["humidity"],
        }
    except Exception as e:
        return {"error": str(e)}


@app.get("/db-check")
async def check_db(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT NOW();"))
        now = result.scalar()
        return {"status": "success", "neon_time": str(now)}
    except Exception as e:
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
