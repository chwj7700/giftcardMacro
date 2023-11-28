from pydantic import BaseModel
from typing import List, Optional

class HmChargeDto(BaseModel):
    id: str
    password: str
    pins: List[str]
