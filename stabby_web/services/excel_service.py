from openpyxl import Workbook
from io import BytesIO


class ExcelService:

    @classmethod
    def generate_knife_excel(cls, knife_list):
        wb = Workbook()

        ws = wb.active
        ws.title = "Knife List"

        ws.append(
            [
                "Brand",
                "Knife",
                "Type",
                "# of Blades",
                "Blade Material",
                "Handle Material",
                "Lock",
                "Deployment",
                "Country",
                "Vendor",
                "Purchased New",
                "Needs Work",
                "Date Entered",
            ]
        )

        # for knife in knife_list:
        #     ws.append([knife.br])

        output = BytesIO()
        wb.save(output)
        output.seek(0)

        return output.getvalue()
