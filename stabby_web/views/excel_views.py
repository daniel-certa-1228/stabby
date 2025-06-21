from django.http import HttpResponse
from stabby_web.services import ExcelService, KnifeService, SharpenerService
from django.contrib.auth.decorators import login_required


@login_required
def export_knife_excel(request):
    knife_queryset = KnifeService.get_knife_queryset()

    excel_file = ExcelService.generate_knife_excel(knife_queryset)

    return _build_excel_response(excel_file, "Knife_List.xlsx")


@login_required
def export_sharpener_excel(request):
    sharpener_queryset = SharpenerService.get_sharpener_queryset()

    excel_file = ExcelService.generate_sharpener_excel(sharpener_queryset)

    return _build_excel_response(excel_file, "Sharpener_List.xlsx")


def _build_excel_response(file_bytes: bytes, filename: str) -> HttpResponse:
    response = HttpResponse(
        file_bytes,
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

    response["Content-Disposition"] = f'attachment; filename="{filename}"'

    return response
