import io

import pandas as pd
from fastapi import APIRouter, Depends, File, HTTPException, Request, UploadFile
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from titanic.adapter.inbound.schemas.titanic_request import TitanicPassengerRequest
from titanic.app.models.passenger_model import TitanicPassenger
from titanic.app.ports.input.titanic_command_port import TitanicCommandPort
from backend.apps.titanic.app.use_cases.train_use_case import JackService

titanic_router = APIRouter(prefix="/titanic", tags=["titanic-command"])

col_map = {
    "PassengerId": "passenger_id",
    "Survived": "survived",
    "Pclass": "pclass",
    "Name": "name",
    "Sex": "sex",
    "Age": "age",
    "SibSp": "sib_sp",
    "Parch": "parch",
    "Ticket": "ticket",
    "Fare": "fare",
    "Cabin": "cabin",
    "Boat": "boat",
    "Embarked": "embarked",
}


def _get_command_port(request: Request) -> TitanicCommandPort:
    port: TitanicCommandPort | None = getattr(request.app.state, "titanic_command_port", None)
    if port is None:
        raise HTTPException(status_code=503, detail="Command port가 초기화되지 않았습니다.")
    return port


@titanic_router.post("/upload")
async def upload_titanic_csv(
    request: Request,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    df = df.where(pd.notnull(df), None)

    await db.execute(delete(TitanicPassenger))

    rows = [
        TitanicPassenger(**{col_map[c]: row[c] for c in col_map if c in row})
        for row in df.to_dict(orient="records")
    ]
    db.add_all(rows)
    await db.commit()

    request.app.state.jack = await JackService.create(db)
    return {"message": f"{len(rows)}개 행이 저장되었습니다."}


@titanic_router.post("/predict")
async def predict_survival(
    req: TitanicPassengerRequest,
    command_port: TitanicCommandPort = Depends(_get_command_port),
):
    return await command_port.predict(req)
