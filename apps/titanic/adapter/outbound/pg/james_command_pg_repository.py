import logging

from backend.apps.titanic.adapter.inbound.api.schemas.james_command_schema import TitanicPassengerRequestSchema
from backend.apps.titanic.app.ports.output.james_command_repository import JamesCommandRepository
from backend.apps.titanic.domain.entities.titanic_entity import TitanicPassenger
from backend.core.database import AsyncSessionLocal

logger = logging.getLogger("james.outbound.james_command_pg_repository")


class JamesCommandPgRepository(JamesCommandRepository):

    async def save_passengers(self, passengers: list[TitanicPassengerRequestSchema]) -> None:
        logger.info("DB 저장 시작 (%d건)", len(passengers))
        batch_size = 100
        async with AsyncSessionLocal() as session:
            try:
                for i in range(0, len(passengers), batch_size):
                    batch = passengers[i:i + batch_size]
                    for p in batch:
                        session.add(TitanicPassenger(
                            passenger_id=int(float(p.passenger_id)),
                            survived=int(float(p.survived)),
                            pclass=int(float(p.pclass)),
                            name=p.name,
                            sex=p.gender,
                            age=float(p.age) if p.age is not None else None,
                            sib_sp=int(float(p.sib_sp)),
                            parch=int(float(p.parch)),
                            ticket=p.ticket,
                            fare=float(p.fare),
                            cabin=p.cabin,
                            embarked=p.embarked,
                        ))
                    await session.flush()
                    logger.info("배치 flush 완료 (%d~%d건)", i + 1, min(i + batch_size, len(passengers)))
                await session.commit()
                logger.info("DB commit 완료 (%d건)", len(passengers))
            except Exception:
                logger.exception("저장 중 오류 발생")
                raise
