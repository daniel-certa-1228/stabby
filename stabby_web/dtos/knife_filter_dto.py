class KnifeFilterDTO:
    def __init__(self, brand):
        self.brand = brand

    def to_dict(self):
        return {
            "brand": self.brand,
        }
