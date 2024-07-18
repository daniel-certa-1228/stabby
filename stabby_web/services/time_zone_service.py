from datetime import timezone
from zoneinfo import ZoneInfo


# FOR FUTURE
class TimeZoneService:

    @classmethod
    def get_now(cls):
        central = ZoneInfo("America/Chicago")

        now = timezone.now().astimezone(central)

        return now
