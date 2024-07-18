from django.utils import timezone
from zoneinfo import ZoneInfo


# FOR FUTURE
class TimeZoneService:

    @classmethod
    def get_now(cls):
        central = ZoneInfo("America/Chicago")

        return timezone.now().astimezone(central)
