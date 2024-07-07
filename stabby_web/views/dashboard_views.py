from stabby_web.dtos import TemplateVariableDTO
from stabby_web.enums import Modules, ViewTypes
from django.conf import settings
from django.shortcuts import render


def index(request):
    variable_dto = TemplateVariableDTO(ViewTypes.Dashboard.value, not settings.DEBUG)

    context = {
        "active": Modules.Dashboard.value,
        "template_variables": variable_dto.to_dict(),
    }

    return render(request, "stabby_web/index.html", context)
