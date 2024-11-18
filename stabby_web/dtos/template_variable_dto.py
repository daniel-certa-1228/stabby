from dataclasses import dataclass
from typing import Optional
from stabby_web.dtos.knife_filter_dto import KnifeFilterDTO


@dataclass
class TemplateVariableDTO:
    view_type: str
    is_production: bool
    knife_id: Optional[int] = None
    sharpener_id: Optional[int] = None
    blade_id: Optional[int] = None
    work_log_id: Optional[int] = None
    photo_id: Optional[int] = None
    knife_filter: Optional["KnifeFilterDTO"] = None

    def to_dict(self):
        return {
            "view_type": self.view_type,
            "is_production": self.is_production,
            "knife_id": self.knife_id,
            "sharpener_id": self.sharpener_id,
            "blade_id": self.blade_id,
            "work_log_id": self.work_log_id,
            "photo_id": self.photo_id,
            "knife_filter": self.knife_filter.to_dict() if self.knife_filter else None,
        }
