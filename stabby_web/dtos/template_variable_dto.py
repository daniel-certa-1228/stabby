class TemplateVariableDTO:
    def __init__(
        self,
        view_type,
        is_production,
        knife_id=None,
        sharpener_id=None,
        blade_id=None,
        work_log_id=None,
        photo_id=None,
        knife_filter=None,
    ):
        self.view_type = view_type
        self.is_production = is_production
        self.knife_id = knife_id
        self.sharpener_id = sharpener_id
        self.blade_id = blade_id
        self.work_log_id = work_log_id
        self.photo_id = photo_id
        self.knife_filter = knife_filter

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
