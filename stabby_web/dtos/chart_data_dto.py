class ChartDataDTO:
    def __init__(self, name, count, percentage, query_str=None):
        self.name = name
        self.count = count
        self.percentage = percentage
        self.query_str = query_str

    def to_dict(self):
        return {
            "name": self.name,
            "count": self.count,
            "percentage": self.percentage,
            "query_str": self.query_str,
        }
