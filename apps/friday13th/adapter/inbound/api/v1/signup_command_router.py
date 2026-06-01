import logging
from fastapi import APIRouter, HTTPException, Request
from sqlalchemy.exc import IntegrityError
from backend.apps.friday13th.adapter.inbound.api.schemas.user_schema import UserSchema
from backend.apps.friday13th.app.ports.input.signup_command_use_case import SignupCommandUseCasePort

logger = logging.getLogger(__name__)

signup_command_router = APIRouter(tags=["user"])


def _get_use_case(request: Request) -> SignupCommandUseCasePort:
    use_case: SignupCommandUseCasePort | None = getattr(request.app.state, "signup_interactor", None)
    if use_case is None:
        raise HTTPException(status_code=503, detail="signup_interactor가 초기화되지 않았습니다.")
    return use_case


@signup_command_router.post("/signup")
async def signup(req: UserSchema, request: Request):
    logger.info("회원가입 요청 수신 — 아이디: %s / 닉네임: %s / 이메일: %s", req.userId, req.nickname, req.email)
    use_case = _get_use_case(request)
    try:
        user = await use_case.save_user(req)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="이미 사용 중인 이메일입니다.")
    return {"message": "회원가입 완료", "userId": user.user_id, "nickname": user.nickname, "email": user.email}
