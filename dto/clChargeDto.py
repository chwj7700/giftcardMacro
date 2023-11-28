from pydantic import BaseModel
from typing import List, Optional

class ClChargeDto(BaseModel):
    id: str
    password: str
    pins: List[str]
