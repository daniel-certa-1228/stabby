from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from stabby_web.dtos import TemplateVariableDTO
from stabby_web.enums import Modules, FormTypes, UnitsOfMeasure, ViewTypes
from stabby_web.forms import KnifeForm, PhotoForm
from stabby_web.services import LibraryService, KnifeService, TimeZoneService
from stabby_web.decorators import skip_save


# MVT VIEWS
@login_required
def library(request):
    library = LibraryService.get_photos_grouped_by_brand()

    variable_dto = TemplateVariableDTO(ViewTypes.Library.value, not settings.DEBUG)

    context = {
        "active": Modules.Library.value,
        "template_variables": variable_dto.to_dict(),
        "library": library,
    }

    return render(request, "stabby_web/library.html", context)
