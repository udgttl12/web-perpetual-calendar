from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.request import CalcRequest
from app.models.response import CalcResponse
from app.services.pillars import calculate_pillars
from app.infra.database import get_session
from app.models.db import CalcSnapshot

router = APIRouter()


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/calc", response_model=CalcResponse)
async def calc(
    request: CalcRequest = Depends(),
    session: Session = Depends(get_session),
) -> CalcResponse:
    result = calculate_pillars(request)
    snapshot = CalcSnapshot(
        date=request.date,
        time=request.time,
        tz=request.tz,
        year=result.year,
        month=result.month,
        day=result.day,
        time_pillar=result.time,
    )
    session.add(snapshot)
    session.commit()
    return result
