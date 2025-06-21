from django.http import HttpResponse
from stabby_web.services import ExcelService, KnifeService, SharpenerService


def export_knife_excel(request):
    knife_queryset = KnifeService.get_knife_queryset()

    excel_file = ExcelService.generate_knife_excel(knife_queryset)

    response = HttpResponse(
        excel_file,
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

    response["Content-Disposition"] = "attachment; filename=Knife_List.xlsx"

    return response


def export_sharpener_excel(request):
    sharpener_queryset = SharpenerService.get_sharpener_queryset()

    excel_file = ExcelService.generate_sharpener_excel(sharpener_queryset)

    response = HttpResponse(
        excel_file,
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

    response["Content-Disposition"] = "attachment; filename=Sharpener_List.xlsx"

    return response
