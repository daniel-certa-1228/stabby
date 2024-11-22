from dataclasses import dataclass
from typing import Optional


@dataclass
class PhotoDTO:
    photo_id: int
    photo_url: str
    description: Optional[str] = None
