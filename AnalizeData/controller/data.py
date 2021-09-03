from pydantic import BaseModel
from datetime import datetime


class AcceptData(BaseModel):
    id: str
    count: int
    date: datetime

