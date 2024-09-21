class KnifeFilterDTO:
    def __init__(
        self,
        brand=None,
        vendor=None,
        blade_material=None,
        handle_material=None,
        purchased_new=None,
        blade_shape_id=None,
    ):
        self.brand = brand
        self.vendor = vendor
        self.blade_material = blade_material
        self.handle_material = handle_material
        self.purchased_new = purchased_new
        self.blade_shape_id = blade_shape_id

    def to_dict(self):
        return {
            "brand": self.brand,
            "vendor": self.vendor,
            "blade_material": self.blade_material,
            "handle_material": self.handle_material,
            "purchased_new": self.purchased_new,
            "blade_shape_id": self.blade_shape_id,
        }
