import datetime
from stabby_web.dtos import ChartDataDTO
from django.db import connection
from django.db.models import Sum
from ..models import (
    Knife,
    LastPurchaseDate,
    Sharpener,
    ViewKnifeGrid,
)


class DashboardService:

    @classmethod
    def get_blade_material_chart_data(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM view_blade_material_chart;")
            rows = cursor.fetchall()

        return cls._map_to_chart_dto(rows)

    @classmethod
    def get_blade_shape_chart_data(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM view_blade_shape_chart;")
            rows = cursor.fetchall()

        return cls._map_to_chart_dto(rows)

    @classmethod
    def get_brand_chart_data(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM view_brand_chart;")
            rows = cursor.fetchall()

        return cls._map_to_chart_dto(rows)

    @classmethod
    def get_country_chart_data(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM view_country_chart;")
            rows = cursor.fetchall()

        return cls._map_to_chart_dto(rows)

    @classmethod
    def get_deployment_type_chart_data(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM view_deployment_type_chart;")
            rows = cursor.fetchall()

        return cls._map_to_chart_dto(rows)

    @classmethod
    def get_handle_material_chart_data(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM view_handle_material_chart;")
            rows = cursor.fetchall()

        return cls._map_to_chart_dto(rows)

    @classmethod
    def get_knife_type_data(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM view_knife_type_chart;")
            rows = cursor.fetchall()

        return cls._map_to_chart_dto(rows)

    @classmethod
    def get_last_purchase_date(cls, now: datetime):
        date_row = cls.get_last_purchase_date_row()

        date = now

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

        return cls._map_to_chart_dto(rows)

    @classmethod
    def get_number_of_days_since_purchase(cls, now: datetime):
        today = now.date()

        date_row = cls.get_last_purchase_date_row()

        stored_date = date_row.last_purchase_date if date_row else today

        diff = (today - stored_date).days

        return diff

    @classmethod
    def get_steel_type_chart_data(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM view_steel_type_chart;")
            rows = cursor.fetchall()

        return cls._map_to_chart_dto(rows)

    @classmethod
    def get_total_blades(cls):
        return ViewKnifeGrid.objects.filter(is_active=True).aggregate(
            total=Sum("num_of_blades")
        )["total"]

    @classmethod
    def get_total_knives(cls):
        return Knife.objects.filter(is_active=True).count()

    @classmethod
    def get_total_new_knives(cls):
        return Knife.objects.filter(is_active=True, purchased_new=True).count()

    @classmethod
    def get_total_used_knives(cls):
        return Knife.objects.filter(is_active=True, purchased_new=False).count()

    @classmethod
    def get_total_sharpeners(cls):
        return Sharpener.objects.filter(is_active=True).count()

    @classmethod
    def get_usa_new_vintage_chart_data(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM view_usa_new_vintage_chart;")
            rows = cursor.fetchall()

        return cls._map_to_chart_dto(rows)

    @classmethod
    def get_vendor_chart_data(cls):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM view_vendor_chart;")
            rows = cursor.fetchall()

        return cls._map_to_chart_dto(rows)

    @classmethod
    def _map_to_chart_dto(cls, rows):
        dtos = list()

        for row in rows:
            dto = ChartDataDTO(
                name=row[0],
                count=row[1],
                percentage=row[2],
                query_str=row[3] if len(row) > 3 and row[3] else None,
            )
            dtos.append(dto.to_dict())

        return dtos

    @classmethod
    def save_date_row(cls, row: LastPurchaseDate):
        return row.save()
