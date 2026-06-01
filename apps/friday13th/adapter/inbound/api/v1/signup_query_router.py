import logging
from fastapi import APIRouter, HTTPException, Request
from backend.apps.friday13th.app.ports.input.signup_query_use_case import SignupQueryUseCasePort

logger = logging.getLogger(__name__)

signup_query_router = APIRouter(tags=["user"])


def _get_use_case(request: Request) -> SignupQueryUseCasePort:
    use_case: SignupQueryUseCasePort | None = getattr(request.app.state, "signup_query_interactor", None)
    if use_case is None:
        raise HTTPException(status_code=503, detail="signup_query_interactor가 초기화되지 않았습니다.")
    return use_case


@signup_query_router.get("/check-email")
async def check_email(email: str, request: Request):
    logger.info("이메일 중복 확인 요청 — email=%s", email)
    use_case = _get_use_case(request)
    available = await use_case.is_email_available(email)
    return {"available": available}
