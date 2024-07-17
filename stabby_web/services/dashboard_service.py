from django.utils import timezone
from stabby_web.dtos import ChartDataDTO
from stabby_web.models.knife_model import Knife
from stabby_web.models.sharpener_model import Sharpener
from stabby_web.models import LastPurchaseDate
from zoneinfo import ZoneInfo
from django.db import connection
from django.db.models import Sum

from stabby_web.models.view_knife_grid import ViewKnifeGrid


class DashboardService:

    @classmethod
    def get_brand_chart_data(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM view_brand_chart;")
            rows = cursor.fetchall()

        dtos = list()

        for row in rows:
            dto = ChartDataDTO(name=row[0], count=row[1], percentage=row[2])
            dtos.append(dto.to_dict())

        return dtos

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
    def get_lock_type_chart_data(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM view_lock_type_chart;")
            rows = cursor.fetchall()

        dtos = list()

        for row in rows:
            dto = ChartDataDTO(name=row[0], count=row[1], percentage=row[2])
            dtos.append(dto.to_dict())

        return dtos

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
    def get_total_blades(cls):
        return ViewKnifeGrid.objects.filter(is_active=True).aggregate(
            total=Sum("num_of_blades")
        )["total"]

    @classmethod
    def get_total_knives(cls):
        return Knife.objects.filter(is_active=True).count()

    @classmethod
    def get_total_sharpeners(cls):
        return Sharpener.objects.filter(is_active=True).count()

    @classmethod
    def save_date_row(cls, row):
        return row.save()
