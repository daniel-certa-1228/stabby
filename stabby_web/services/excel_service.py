from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, numbers
from openpyxl.utils import get_column_letter
from io import BytesIO


class ExcelService:

    @classmethod
    def generate_knife_excel(cls, knife_queryset):
        wb = Workbook()

        ws = wb.active
        ws.title = "Knife List"

        header_font = Font(bold=True, color="FFFFFF")
        header_fill = PatternFill(
            fill_type="solid", start_color="000000", end_color="000000"
        )

        headers = [
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

        ws.append(headers)

        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=1, column=col)
            cell.font = header_font
            cell.fill = header_fill

        for row_idx, knife in enumerate(knife_queryset, start=2):
            col = 1
            ws.cell(row=row_idx, column=col, value=knife.brand)
            col += 1
            ws.cell(row=row_idx, column=col, value=knife.knife)
            col += 1
            ws.cell(row=row_idx, column=col, value=knife.knife_type)
            col += 1
            ws.cell(row=row_idx, column=col, value=knife.num_of_blades)
            col += 1
            ws.cell(row=row_idx, column=col, value=knife.blade_material)
            col += 1
            ws.cell(row=row_idx, column=col, value=knife.handle_material)
            col += 1
            ws.cell(row=row_idx, column=col, value=knife.lock_type)
            col += 1
            ws.cell(row=row_idx, column=col, value=knife.deployment_type)
            col += 1
            ws.cell(row=row_idx, column=col, value=knife.country)
            col += 1
            ws.cell(row=row_idx, column=col, value=knife.vendor)
            col += 1
            # Purchased New bool column
            purchased_new_value = "New" if knife.purchased_new else "Used"
            pn_font = Font(color="A0A0A0") if not knife.purchased_new else None

            cell = ws.cell(row=row_idx, column=col, value=purchased_new_value)

            if pn_font:
                cell.font = pn_font

            col += 1

            # Needs Work bool column
            needs_work_value = "Yes" if knife.needs_work else "No"
            nw_font = Font(color="A0A0A0") if not knife.needs_work else None

            cell = ws.cell(row=row_idx, column=col, value=needs_work_value)

            if nw_font:
                cell.font = nw_font

            col += 1
            # Date col
            date_cell = ws.cell(
                row=row_idx, column=col, value=knife.create_date.replace(tzinfo=None)
            )
            date_cell.number_format = "m/d/yyyy"
            col += 1

        # Hack for auto-width
        num_columns = len(headers)

        for col_idx in range(1, num_columns + 1):
            col_letter = get_column_letter(col_idx)
            max_length = 0

            for row in ws.iter_rows(
                min_row=1, max_row=ws.max_row, min_col=col_idx, max_col=col_idx
            ):
                for cell in row:
                    if cell.value:
                        try:
                            max_length = max(max_length, len(str(cell.value).strip()))
                        except:
                            pass

            ws.column_dimensions[col_letter].width = max_length

        # Manual widths for problem columns
        column_map = {
            "Deployment": 13,
            "Purchased New": 15,
            "Needs Work": 13,
            "Date Entered": 15,
        }
        for header_name, width in column_map.items():
            col_letter = get_column_letter(headers.index(header_name) + 1)
            ws.column_dimensions[col_letter].width = width

        ws.freeze_panes = "A2"

        output = BytesIO()
        wb.save(output)
        output.seek(0)

        return output.getvalue()
