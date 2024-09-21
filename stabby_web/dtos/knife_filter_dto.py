class KnifeFilterDTO:
    def __init__(
        self,
        brand=None,
        vendor=None,
        blade_material=None,
        handle_material=None,
        blade_shape_id=None,
    ):
        self.brand = brand
        self.vendor = vendor
        self.blade_material = blade_material
        self.handle_material = handle_material
        self.blade_shape_id = blade_shape_id

    def to_dict(self):
        return {
            "brand": self.brand,
            "vendor": self.vendor,
            "blade_material": self.blade_material,
            "handle_material": self.handle_material,
            "blade_shape_id": self.blade_shape_id,
        }
