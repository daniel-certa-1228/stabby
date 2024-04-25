from django.http import JsonResponse
from ..services import DbService


# JSON VIEWS
def get_knife_work_log_grid(request, knife_id):
    data = DbService.get_knife_work_log_grid(knife_id)

    return JsonResponse(data, safe=False)


def get_sharpener_work_log_grid(request, sharpener_id):
    data = DbService.get_sharpener_work_log_grid(sharpener_id)

    return JsonResponse(data, safe=False)
