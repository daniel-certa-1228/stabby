from django.utils import timezone
from stabby_web.dtos import ChartDataDTO
from ..models import LastPurchaseDate
from zoneinfo import ZoneInfo
from django.db import connection


class DashboardService:

    @classmethod
    def get_country_chart_data(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM view_country_chart;")
            rows = cursor.fetchall()

        dtos = list()

        for row in rows:
            dto = ChartDataDTO(name=row[0], count=row[1], percentage=row[2])
            dtos.append(dto.to_dict())

        return dtos

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
    def get_steel_type_chart_data(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM view_steel_type_chart;")
            rows = cursor.fetchall()

        dtos = list()

        for row in rows:
            dto = ChartDataDTO(name=row[0], count=row[1], percentage=row[2])
            dtos.append(dto.to_dict())

        return dtos

    @classmethod
    def save_date_row(cls, row):
        return row.save()
