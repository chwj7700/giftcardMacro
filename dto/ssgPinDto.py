from pydantic import BaseModel
from typing import List, Optional

class SsgPinDto(BaseModel):
    id: str
    password: str
