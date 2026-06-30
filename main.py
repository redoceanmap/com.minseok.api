import asyncio
import logging
import sys
import os
from contextlib import asynccontextmanager

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "apps"))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.matrix.grid_oracle_database_manager import dispose_engine, init_engine, create_all_tables
from titanic.adapter.inbound.api import titanic_router
from sherlock_homes.adapter.inbound.api import sherlock_router


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:\t%(message)s",
        force=True,
    )


_configure_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_engine()
    await create_all_tables()
    try:
        yield
    finally:
        await dispose_engine()


app = FastAPI(title="MinSeok Main", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(titanic_router, prefix="/api")
app.include_router(sherlock_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "FAST API 메인 페이지 ", "docs": "/docs"}


if __name__ == "__main__":
    import uvicorn

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    uvicorn.run("main:app", host="127.0.0.1", port=8000, loop="none")
