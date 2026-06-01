import io
import logging

import pandas as pd
from fastapi import APIRouter, File, HTTPException, Request, UploadFile

from backend.apps.titanic.adapter.inbound.api.schemas.james_command_schema import TitanicPassengerRequestSchema
from backend.apps.titanic.app.ports.input.james_command_use_case import JamesCommandUseCase

logger = logging.getLogger("james.inbound.james_command_router")

james_command_router = APIRouter(prefix="/titanic/james", tags=["james"])

EXPECTED_COLUMNS = {
    "PassengerId", "Survived", "Pclass", "Name", "Sex",
    "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked",
}


def _get_use_case(request: Request) -> JamesCommandUseCase:
    use_case: JamesCommandUseCase | None = request.app.state.james
    if use_case is None:
        raise HTTPException(status_code=503, detail="james use case가 초기화되지 않았습니다.")
    return use_case


@james_command_router.post("/upload")
async def upload_csv(request: Request, file: UploadFile = File(...)):
    logger.info("CSV 수신 (파일명: %s)", file.filename)

    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="CSV 파일만 업로드할 수 있습니다.")

    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    logger.info("CSV 파싱 완료 (%d행), DTO 변환 시작", len(df))

    missing = EXPECTED_COLUMNS - set(df.columns)
    if missing:
        raise HTTPException(status_code=422, detail=f"필수 컬럼 누락: {missing}")

    df = df.rename(columns={"Sex": "Gender"})

    passengers = [
        TitanicPassengerRequestSchema(
            passenger_id=str(row["PassengerId"]),
            survived=str(row["Survived"]),
            pclass=str(row["Pclass"]),
            name=str(row["Name"]),
            gender=str(row["Gender"]),
            age=str(row["Age"]) if pd.notna(row.get("Age")) else None,
            sib_sp=str(row["SibSp"]),
            parch=str(row["Parch"]),
            ticket=str(row["Ticket"]),
            fare=str(row["Fare"]),
            cabin=str(row["Cabin"]) if pd.notna(row.get("Cabin")) else None,
            embarked=str(row["Embarked"]) if pd.notna(row.get("Embarked")) else None,
        )
        for _, row in df.iterrows()
    ]
    logger.info("DTO 변환 완료 (%d건)", len(passengers))

    use_case = _get_use_case(request)
    result = await use_case.upload_passengers(passengers)
    preview = df.head(5).replace({float("nan"): None}).to_dict(orient="records")
    result["preview"] = preview
    logger.info("[제임스 라우터] 업로드된 CSV 파일에서 파싱된 상위 5개 레코드: %s", preview)
    logger.info("응답 반환")
    return result
