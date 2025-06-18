from django.http import HttpResponse
from stabby_web.services import ExcelService, KnifeService


def export_knife_excel(request):
    knife_list = KnifeService.get_knife_grid(request)

    excel_file = ExcelService.generate_knife_excel(knife_list)

    response = HttpResponse(
        excel_file,
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

    response["Content-Disposition"] = "attachment; filename=Knife_List.xlsx"

    return response
