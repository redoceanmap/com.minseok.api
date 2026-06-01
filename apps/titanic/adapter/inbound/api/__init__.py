from fastapi import APIRouter

from titanic.adapter.inbound.api.v1.andrews_query_router import andrews_query_router
from titanic.adapter.inbound.api.v1.cal_query_router import cal_query_router
from titanic.adapter.inbound.api.v1.hartlery_query_router import hartlery_query_router
from titanic.adapter.inbound.api.v1.isidor_query_router import isidor_query_router
from titanic.adapter.inbound.api.v1.jack_query_router import jack_query_router
from titanic.adapter.inbound.api.v1.james_command_router import james_command_router
from titanic.adapter.inbound.api.v1.model_query_router import model_query_router
from titanic.adapter.inbound.api.v1.passenger_query_router import passenger_query_router
from titanic.adapter.inbound.api.v1.rose_query_router import rose_query_router
from titanic.adapter.inbound.api.v1.ruth_query_router import ruth_query_router
from titanic.adapter.inbound.api.v1.smith_query_router import smith_query_router
from titanic.adapter.inbound.api.v1.walter_query_router import walter_query_router

titanic_router = APIRouter()
titanic_router.include_router(andrews_query_router)
titanic_router.include_router(cal_query_router)
titanic_router.include_router(hartlery_query_router)
titanic_router.include_router(isidor_query_router)
titanic_router.include_router(jack_query_router)
titanic_router.include_router(james_command_router)
titanic_router.include_router(model_query_router)
titanic_router.include_router(passenger_query_router)
titanic_router.include_router(rose_query_router)
titanic_router.include_router(ruth_query_router)
titanic_router.include_router(smith_query_router)
titanic_router.include_router(walter_query_router)
