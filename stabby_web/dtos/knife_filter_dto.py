from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class KnifeFilterDTO:
    brand: Optional[str] = None
    vendor: Optional[str] = None
    blade_material: Optional[str] = None
    handle_material: Optional[str] = None
    knife_type: Optional[str] = None
    purchased_new: Optional[bool] = None
    blade_shape_id: Optional[int] = None

    def to_dict(self):
        return asdict(self)
