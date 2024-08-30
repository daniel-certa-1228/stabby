class KnifeFilterDTO:
    def __init__(self, brand=None, vendor=None):
        self.brand = brand
        self.vendor = vendor

    def to_dict(self):
        return {"brand": self.brand, "vendor": self.vendor}
