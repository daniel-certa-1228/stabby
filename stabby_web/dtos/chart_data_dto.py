from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class ChartDataDTO:
    name: str
    count: int
    percentage: float
    query_str: Optional[str] = None

    def to_dict(self):
        return asdict(self)
