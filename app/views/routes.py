from __future__ import annotations

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from app.models.request import CalcRequest
from app.services.pillars import calculate_pillars
from app.infra.database import get_session
from app.models.db import CalcSnapshot

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(
    request: Request,
    date: str | None = None,
    time: str | None = None,
    tz: str = "Asia/Seoul",
    session: Session = Depends(get_session),
) -> HTMLResponse:
    if date and time:
        req = CalcRequest(date=date, time=time, tz=tz)
        result = calculate_pillars(req)
        snapshot = CalcSnapshot(
            date=req.date,
            time=req.time,
            tz=req.tz,
            year=result.year,
            month=result.month,
            day=result.day,
            time_pillar=result.time,
        )
        session.add(snapshot)
        session.commit()
        return templates.TemplateResponse(
            "result.html", {"request": request, "result": result}
        )
    return templates.TemplateResponse("index.html", {"request": request})
