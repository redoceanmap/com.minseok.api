import logging

import dataclasses

from sqlalchemy import delete

from backend.apps.titanic.app.dtos.james_dto import PersonCommand, BookingCommand
from backend.apps.titanic.app.ports.output.james_command_repository import JamesCommandRepository
from backend.apps.titanic.domain.entities.titanic_entity import TitanicPassenger
from backend.core.database import AsyncSessionLocal


logger = logging.getLogger(__name__)


class JamesCommandPgRepository(JamesCommandRepository):

    async def save_passengers(self, person: list[PersonCommand], bookings: list[BookingCommand]) -> None:
        total = len(person)
        batch_size = 100
        total_batches = (total + batch_size - 1) // batch_size
        logger.info("DB 저장 시작 (총 %d건, %d배치)", total, total_batches)
        person_preview = [dataclasses.asdict(p) for p in person[:5]]
        booking_preview = [dataclasses.asdict(b) for b in bookings[:5]]
        logger.info("[제임스 레포지토리] PersonCommand 상위 5개 레코드: %s", person_preview)
        logger.info("[제임스 레포지토리] BookingCommand 상위 5개 레코드: %s", booking_preview)
        async with AsyncSessionLocal() as session:
            try:
                logger.info("기존 데이터 삭제 시작")
                await session.execute(delete(TitanicPassenger))
                logger.info("기존 데이터 삭제 완료")
                for i in range(0, total, batch_size):
                    batch_persons = person[i:i + batch_size]
                    batch_bookings = bookings[i:i + batch_size]
                    batch_num = i // batch_size + 1
                    logger.info("배치 %d/%d 처리 시작 (%d건)", batch_num, total_batches, len(batch_persons))
                    for p, b in zip(batch_persons, batch_bookings):
                        session.add(TitanicPassenger(
                            passenger_id=int(float(p.passenger_id)),
                            survived=int(float(p.survived)),
                            pclass=int(float(b.pclass)),
                            name=p.name,
                            sex=p.gender,
                            age=float(p.age) if p.age is not None else None,
                            sib_sp=int(float(p.sib_sp)),
                            parch=int(float(p.parch)),
                            ticket=b.ticket,
                            fare=float(b.fare),
                            cabin=b.cabin,
                            embarked=b.embarked,
                        ))
                    await session.flush()
                    logger.info("배치 %d/%d flush 완료", batch_num, total_batches)
                await session.commit()
                logger.info("DB commit 완료 (총 %d건)", total)
            except Exception:
                logger.exception("저장 중 오류 발생")
                raise
