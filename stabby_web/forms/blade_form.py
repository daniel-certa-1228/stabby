from django import forms
from ..models import Blade
from ..services import DropdownService


class BladeForm(forms.ModelForm):

    class Meta:
        model = Blade
        exclude = ["create_date", "edit_date", "is_active", "knife"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap class to form fields
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control form-control-sm mb-2"

            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs["rows"] = 3

        self.fields["blade_shape"].queryset = DropdownService.get_blade_shapes()
        self.fields["uom"].queryset = DropdownService.get_units_of_measure()

        self.fields["blade_shape"].label = "Blade Shape"
        self.fields["blade_shape_notes"].label = "Blade Shape Notes"
        self.fields["is_main_blade"].label = "Is Main Blade"
        self.fields["blade_shape"].label = "Blade Shape"
        self.fields["blade_shape"].empty_label = "Select Blade Shape"
        self.fields["length_cutting_edge"].label = "Cutting Edge Length"
        self.fields["uom"].label = "UOM"
        self.fields["uom"].empty_label = "Select UOM"

    def clean_blade_shape_notes(self):
        blade_shape_notes = self.cleaned_data.get("blade_shape_notes")
        if blade_shape_notes:
            return blade_shape_notes.strip()
        return blade_shape_notes
