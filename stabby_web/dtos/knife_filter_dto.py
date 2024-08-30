class KnifeFilterDTO:
    def __init__(self, brand=None, vendor=None, blade_material=None):
        self.brand = brand
        self.vendor = vendor
        self.blade_material = blade_material

    def to_dict(self):
        return {
            "brand": self.brand,
            "vendor": self.vendor,
            "blade_material": self.blade_material,
        }
