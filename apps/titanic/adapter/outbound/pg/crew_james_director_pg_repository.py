from __future__ import annotations
import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert

from titanic.adapter.outbound.orm.passenger_rose_model_orm import RoseModelOrm as BookingOrm
from titanic.adapter.outbound.orm.passenger_jack_trainer_orm import JackTrainerOrm as PersonOrm
from titanic.app.dtos.crew_james_director_dto import BookingCommand, JamesDirectorQuery, JamesDirectorResponse, PassengerCommand
from titanic.app.ports.output.crew_james_director_repository import JamesDirectorRepository

logger = logging.getLogger(__name__)

class JamesDirectorPgRepository(JamesDirectorRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: JamesDirectorQuery) -> JamesDirectorResponse:
        
        '''제임스 감독의 자기 소개 레포지토리 구현 메소드'''

        logger.info(f"[JamesDirectorPgRepository] introduce_myself 진입 | request_data={query}")
        
        response: JamesDirectorResponse = JamesDirectorResponse(
            id= query.id * 10000,
            name= query.name + "가 레포지토리에 다녀옴"
        )
        return response

    async def receive_uploaded_records(
        self,
        person_commands: list[PassengerCommand],
        booking_commands: list[BookingCommand],
    ) -> int:
        person_values = [
            {
                "passenger_id": cmd.passenger_id,
                "name": cmd.name,
                "gender": cmd.gender,
                "age": cmd.age,
                "sib_sp": cmd.sib_sp,
                "parch": cmd.parch,
                "survived": cmd.survived,
            }
            for cmd in person_commands
        ]
        await self.session.execute(
            insert(PersonOrm).values(person_values).on_conflict_do_nothing(index_elements=["passenger_id"])
        )
        await self.session.flush()

        booking_values = [
            {
                "passenger_id": cmd_p.passenger_id,
                "pclass": cmd_b.pclass,
                "ticket": cmd_b.ticket,
                "fare": cmd_b.fare,
                "cabin": cmd_b.cabin,
                "embarked": cmd_b.embarked,
            }
            for cmd_p, cmd_b in zip(person_commands, booking_commands)
        ]
        await self.session.execute(
            insert(BookingOrm).values(booking_values).on_conflict_do_nothing(index_elements=["id"])
        )
        await self.session.commit()

        return len(person_values)
