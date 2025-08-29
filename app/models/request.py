from datetime import date, time
from pydantic import BaseModel, Field


class CalcRequest(BaseModel):
    date: date
    time: time
    tz: str = Field(default="Asia/Seoul", description="Timezone identifier")
