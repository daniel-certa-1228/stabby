from django.http import JsonResponse
from ..services import BladeService


# JSON VIEWS
def get_blade_grid(request, knife_id):
    data = BladeService.get_blade_grid(knife_id)

    return JsonResponse(data, safe=False)
