from pydantic import BaseModel


class CalcResponse(BaseModel):
    year: str
    month: str
    day: str
    time: str
