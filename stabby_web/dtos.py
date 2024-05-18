class TemplateVariableDTO:
    def __init__(self, view_type, knife_id, sharpener_id, blade_id, work_log_id, photo_id):
        self.view_type = view_type
        self.knife_id = knife_id
        self.sharpener_id = sharpener_id
        self.blade_id = blade_id
        self.work_log_id = work_log_id,
        self.photo_id = photo_id

    def to_dict(self):
        return {
            "view_type": self.view_type,
            "knife_id": self.knife_id,
            "sharpener_id": self.sharpener_id,
            "blade_id": self.blade_id,
            "work_log_id": self.work_log_id,
            "photo_id": self.photo_id
        }
