from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

from app.core.pillars import pillars_from_datetime
from app.models.request import CalcRequest
from app.models.response import CalcResponse


def calculate_pillars(req: CalcRequest) -> CalcResponse:
    dt = datetime.combine(req.date, req.time).replace(tzinfo=ZoneInfo(req.tz))
    data = pillars_from_datetime(dt)
    return CalcResponse(**data)
