import logging
import os
from contextlib import asynccontextmanager
from pathlib import Path

import httpx
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import json
from database import AsyncSessionLocal, get_db
from matrix.app.keymaker import get_keymaker, GEMINI_MODEL
from secom.app.controllers.user_controller import UserController
from secom.app.schemas.user_schema import LoginSchema, UserSchema
from titanic.adapter.inbound.api.v1.titanic_command_router import titanic_router as titanic_command_router
from titanic.adapter.inbound.api.v1.titanic_query_router import titanic_router as titanic_query_router
from backend.apps.titanic.app.use_cases.train_use_case import JackService
from doro.app.doro_director import DoroDiretor

logger = logging.getLogger("uvicorn.error")

load_dotenv(Path(__file__).parents[1] / ".env")


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncSessionLocal() as session:
        app.state.jack = await JackService.create(session)
    yield


app = FastAPI(title="Main page", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://127.0.0.1:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(titanic_command_router)
app.include_router(titanic_query_router)

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


# 회원가입
@app.post("/signup")
async def signup(req: UserSchema, db: AsyncSession = Depends(get_db)):
    logger.info(
        "회원가입 요청 수신 — 아이디: %s / 닉네임: %s / 이메일: %s",
        req.userId, req.nickname, req.email,
    )

    user_controller = UserController()
    try:
        user = await user_controller.save_user(db, req)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="이미 사용 중인 이메일입니다.")

    return {"message": "회원가입 완료", "userId": user.user_id, "nickname": user.nickname, "email": user.email}


# 로그인
@app.post("/login")
async def login(req: LoginSchema, db: AsyncSession = Depends(get_db)):
    logger.info("로그인 요청 수신 — 이메일: %s", req.email)

    user_controller = UserController()
    user = await user_controller.login_user(db, req)

    if user is None:
        raise HTTPException(status_code=401, detail="이메일 또는 비밀번호가 잘못되었습니다.")

    return {"access_token": "mock-token", "email": user.email, "name": user.nickname}


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


@app.get("/doro/data")
def read_doro_data():
    doro_director = DoroDiretor()
    df = doro_director.get_data() 
    
    return df.to_dict(orient="records")

@app.get("/check-email")
async def check_email(email: str, db: AsyncSession = Depends(get_db)):
    from sqlalchemy import select
    from secom.app.models.user_model import UserModel
    result = await db.execute(select(UserModel).where(UserModel.email == email))
    user = result.scalars().first()
    return {"available": user is None}


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

    