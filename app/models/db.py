from __future__ import annotations

from datetime import date, time, datetime
from sqlmodel import SQLModel, Field


class CalcSnapshot(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    date: date
    time: time
    tz: str
    year: str
    month: str
    day: str
    time_pillar: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
