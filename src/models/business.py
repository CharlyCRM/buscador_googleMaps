from dataclasses import dataclass
from typing import Optional

@dataclass
class Business:
    name: str
    schedule: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None 