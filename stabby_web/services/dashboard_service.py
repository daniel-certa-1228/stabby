from django.utils import timezone
from ..models import LastPurchaseDate
from zoneinfo import ZoneInfo


class DashboardService:

    @classmethod
    def get_last_purchase_date(cls):
        date_row = cls.get_last_purchase_date_row()
        date = timezone.now()

        if date_row is not None and date_row.last_purchase_date is not None:
            date = date_row.last_purchase_date if date_row else None

        return date

    @classmethod
    def get_last_purchase_date_row(cls):
        return LastPurchaseDate.objects.first()

    @classmethod
    def get_number_of_days_since_purchase(cls):
        central = ZoneInfo("America/Chicago")

        today = timezone.now().astimezone(central).date()

        date_row = cls.get_last_purchase_date_row()

        stored_date = date_row.last_purchase_date if date_row else today

        diff = (today - stored_date).days

        return diff

    @classmethod
    def save_date_row(cls, row):
        return row.save()
