import logging
from fastapi import APIRouter, HTTPException, Request
from backend.apps.friday13th.adapter.inbound.api.schemas.user_schema import LoginSchema
from backend.apps.friday13th.app.ports.input.login_command_use_case import LoginCommandUseCasePort

logger = logging.getLogger(__name__)

login_command_router = APIRouter(tags=["auth"])


def _get_use_case(request: Request) -> LoginCommandUseCasePort:
    use_case: LoginCommandUseCasePort | None = getattr(request.app.state, "login_interactor", None)
    if use_case is None:
        raise HTTPException(status_code=503, detail="login_interactor가 초기화되지 않았습니다.")
    return use_case


@login_command_router.post("/login")
async def login(req: LoginSchema, request: Request):
    logger.info("로그인 요청 수신 — 이메일: %s", req.email)
    use_case = _get_use_case(request)
    user = await use_case.login_user(req)
    if user is None:
        raise HTTPException(status_code=401, detail="이메일 또는 비밀번호가 잘못되었습니다.")
    return {"access_token": "mock-token", "email": user.email, "name": user.nickname}
