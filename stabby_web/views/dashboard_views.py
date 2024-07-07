from stabby_web.dtos import TemplateVariableDTO
from stabby_web.enums import Modules, ViewTypes
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from stabby_web.services import DashboardService


# MVT VIEWS
@login_required
def index(request):
    variable_dto = TemplateVariableDTO(ViewTypes.Dashboard.value, not settings.DEBUG)

    last_purchase_date = DashboardService.get_last_purchase_date()

    context = {
        "active": Modules.Dashboard.value,
        "template_variables": variable_dto.to_dict(),
        "last_purchase_date": last_purchase_date,
    }

    return render(request, "stabby_web/index.html", context)
