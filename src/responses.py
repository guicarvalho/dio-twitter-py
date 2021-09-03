from pydantic import BaseModel


class TrendItem(BaseModel):
    name: str
    url: str
