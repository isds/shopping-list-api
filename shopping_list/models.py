from decimal import Decimal
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel


class Item(BaseModel):
    id: Optional[str] = str(uuid4())
    name: str
    quantity: int
    value: Decimal
