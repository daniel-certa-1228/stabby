from stabby_web.dtos import TemplateVariableDTO
from stabby_web.enums import Modules, ViewTypes
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from stabby_web.services import DashboardService, TimeZoneService
from stabby_web.decorators import skip_save
from stabby_web.custom_encoders import DecimalEncoder
from django.http import JsonResponse
import json


# MVT VIEWS
@login_required
def index(request):
    variable_dto = TemplateVariableDTO(ViewTypes.Dashboard.value, not settings.DEBUG)

    now = TimeZoneService.get_now()

    last_purchase_date = DashboardService.get_last_purchase_date(now)

    total_knives = DashboardService.get_total_knives()

    total_new_knives = DashboardService.get_total_new_knives()

    total_used_knives = DashboardService.get_total_used_knives()

    new_percentage = (
        f"{(total_new_knives / total_knives if total_knives > 0 else 0) * 100:.2f}%"
    )

    used_percentage = (
        f"{(total_used_knives / total_knives if total_knives > 0 else 0) * 100:.2f}%"
    )

    total_blades = DashboardService.get_total_blades()

    total_sharpeners = DashboardService.get_total_sharpeners()

    brand_breakdown = DashboardService.get_brand_chart_data()

    vendor_breakdown = DashboardService.get_vendor_chart_data()

    blade_material_breakdown = DashboardService.get_blade_material_chart_data()

    handle_material_breakdown = DashboardService.get_handle_material_chart_data()

    context = {
        "active": Modules.Dashboard.value,
        "template_variables": variable_dto.to_dict(),
        "last_purchase_date": last_purchase_date,
        "total_knives": total_knives,
        "total_new_knives": total_new_knives,
        "total_used_knives": total_used_knives,
        "new_percentage": new_percentage,
        "used_percentage": used_percentage,
        "total_blades": total_blades,
        "total_sharpeners": total_sharpeners,
        "brand_breakdown": brand_breakdown,
        "blade_material_breakdown": blade_material_breakdown,
        "handle_material_breakdown": handle_material_breakdown,
        "vendor_breakdown": vendor_breakdown,
    }

    return render(request, "stabby_web/index.html", context)


# JSON VIEWS
@login_required
def get_country_chart_data(request):
    data = DashboardService.get_country_chart_data()

    return JsonResponse(data, safe=False, encoder=DecimalEncoder)


@login_required
def get_lock_type_chart_data(request):
    data = DashboardService.get_lock_type_chart_data()

    return JsonResponse(data, safe=False, encoder=DecimalEncoder)


@login_required
def get_steel_type_chart_data(request):
    data = DashboardService.get_steel_type_chart_data()

    return JsonResponse(data, safe=False, encoder=DecimalEncoder)


@skip_save
@login_required
def set_last_purchase_date(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            selected_date = data.get("date")

            row = DashboardService.get_last_purchase_date_row()

            if row is not None and selected_date is not None:
                row.last_purchase_date = selected_date

                if request.is_collector:
                    DashboardService.save_date_row(row)

                return JsonResponse(True, safe=False)
            else:
                return JsonResponse(False, safe=False)

        except Exception as e:
            print(e)
            return JsonResponse(False, safe=False)
    else:
        return JsonResponse(False, safe=False)
