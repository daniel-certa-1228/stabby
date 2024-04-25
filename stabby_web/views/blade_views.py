from django.http import JsonResponse
from ..services import DbService


# JSON VIEWS
def get_blade_grid(request, knife_id):
    data = DbService.get_blade_grid(knife_id)

    return JsonResponse(data, safe=False)
