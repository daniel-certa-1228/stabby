from django import forms
from ..models import Sharpener
from ..services import DropdownService


class SharpenerForm(forms.ModelForm):

    class Meta:
        model = Sharpener
        exclude = ["create_date", "edit_date", "is_active", "user"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap class to form fields
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control form-control-sm mb-2"

            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs["rows"] = 4

        self.fields["bonding_agent"].queryset = DropdownService.get_bonding_agents()
        self.fields["brand"].queryset = DropdownService.get_brands()
        self.fields["country"].queryset = DropdownService.get_countries()
        self.fields["cutting_agent"].queryset = DropdownService.get_cutting_agents()
        self.fields["lubricant"].queryset = DropdownService.get_lubricants()
        self.fields["uom"].queryset = DropdownService.get_units_of_measure()

        self.fields["brand"].empty_label = "Select Brand"
        self.fields["brand_notes"].label = "Brand Notes"
        self.fields["bonding_agent"].label = "Bonding Agent"
        self.fields["bonding_agent"].empty_label = "Select Bonding Agent"
        self.fields["cutting_agent"].label = "Cutting Agent"
        self.fields["cutting_agent"].empty_label = "Select Cutting Agent"
        self.fields["country"].empty_label = "Select Country"
        self.fields["lubricant"].empty_label = "Select Lubricant"
        self.fields["name"].label = "Sharpener"
        self.fields["uom"].label = "UOM"
        self.fields["uom"].empty_label = "Select UOM"

    def clean_brand_notes(self):
        brand_notes = self.cleaned_data.get("brand_notes")
        if brand_notes:
            return brand_notes.strip()
        return brand_notes

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name:
            return name.strip()
        return name

    def clean_notes(self):
        notes = self.cleaned_data.get("notes")
        if notes:
            return notes.strip()
        return notes
