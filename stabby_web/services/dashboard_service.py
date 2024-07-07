from django.utils import timezone
from ..models import LastPurchaseDate


class DashboardService:

    @classmethod
    def get_last_purchase_date(cls):
        date_row = LastPurchaseDate.objects.first()
        date = timezone.now()

        if date_row is not None and date_row.last_purchase_date is not None:
            date = date_row.last_purchase_date if date_row else None

        return date
