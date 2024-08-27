class ChartDataDTO:
    def __init__(self, name, count, percentage):
        self.name = name
        self.count = count
        self.percentage = percentage

    def to_dict(self):
        return {
            "name": self.name,
            "count": self.count,
            "percentage": self.percentage,
        }
