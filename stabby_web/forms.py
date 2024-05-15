from django import forms
from .models import Blade, Knife, Sharpener, WorkLog
from .services import DropdownService


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


class KnifeForm(forms.ModelForm):

    class Meta:
        model = Knife
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
                field.widget.attrs["rows"] = 3

        self.fields["blade_material"].queryset = DropdownService.get_blade_materials()
        self.fields["brand"].queryset = DropdownService.get_brands()
        self.fields["country"].queryset = DropdownService.get_countries()
        self.fields["deployment_type"].queryset = DropdownService.get_deployment_types()
        self.fields["handle_material"].queryset = DropdownService.get_handle_materials()
        self.fields["knife_type"].queryset = DropdownService.get_knife_types()
        self.fields["lock_type"].queryset = DropdownService.get_lock_types()
        self.fields["uom"].queryset = DropdownService.get_units_of_measure()
        self.fields["vendor"].queryset = DropdownService.get_vendors()

        self.fields["blade_material"].label = "Blade Material"
        self.fields["blade_material_notes"].label = "Blade Material Notes"
        self.fields["blade_material"].empty_label = "Select Blade Material"
        self.fields["brand"].empty_label = "Select Brand"
        self.fields["brand_notes"].label = "Brand Notes"
        self.fields["closed_length"].label = "Closed Length"
        self.fields["country"].empty_label = "Select Country"
        self.fields["deployment_type"].label = "Deployment Type"
        self.fields["deployment_type"].empty_label = "Select Deployment Type"
        self.fields["handle_material"].label = "Handle Material"
        self.fields["handle_material"].empty_label = "Select Handle Material"
        self.fields["handle_material_notes"].label = "Handle Material Notes"
        self.fields["knife_type"].label = "Knife Type"
        self.fields["knife_type"].empty_label = "Select Knife Type"
        self.fields["knife_type_notes"].label = "Knife Type Notes"
        self.fields["lock_type"].label = "Lock Type"
        self.fields["lock_type"].empty_label = "Select Lock Type"
        self.fields["lock_type_notes"].label = "Lock Type Notes"
        self.fields["name"].label = "Knife"
        self.fields["needs_work"].label = "Needs Work"
        self.fields["notes"].label = "General Notes"
        self.fields["purchased_new"].label = "Purchased New"
        self.fields["uom"].label = "UOM"
        self.fields["uom"].empty_label = "Select UOM"
        self.fields["year_of_manufacture"].label = "Year Manufactured"
        self.fields["vendor"].empty_label = "Select Vendor"
        self.fields["year_of_purchase"].label = "Year Purchased"

        def clean_blade_material_notes(self):
            blade_material_notes = self.cleaned_data.get("blade_material_notes")
            if blade_material_notes:
                return blade_material_notes.strip()
            return blade_material_notes

        def clean_brand_notes(self):
            brand_notes = self.cleaned_data.get("brand_notes")
            if brand_notes:
                return brand_notes.strip()
            return brand_notes

        def clean_handle_material_notes(self):
            handle_material_notes = self.cleaned_data.get("handle_material_notes")
            if handle_material_notes:
                return handle_material_notes.strip()
            return handle_material_notes

        def clean_knife_type_notes(self):
            knife_type_notes = self.cleaned_data.get("knife_type_notes")
            if knife_type_notes:
                return knife_type_notes.strip()
            return knife_type_notes

        def clean_lock_type_notes(self):
            lock_type_notes = self.cleaned_data.get("lock_type_notes")
            if lock_type_notes:
                return lock_type_notes.strip()
            return lock_type_notes

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

        def clean_year_of_manufacture(self):
            year_of_manufacture = self.cleaned_data.get("year_of_manufacture")
            if year_of_manufacture:
                return year_of_manufacture.strip()
            return year_of_manufacture

        def clean_year_of_purchase(self):
            year_of_purchase = self.cleaned_data.get("year_of_purchase")
            if year_of_purchase:
                return year_of_purchase.strip()
            return year_of_purchase


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


class WorkLogForm(forms.ModelForm):

    class Meta:
        model = WorkLog
        exclude = ["create_date", "edit_date", "is_active", "knife", "sharpener"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap class to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control form-control-sm mb-2"

            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs["rows"] = 4

    date = forms.DateTimeField(
        label="Date",
        required=True,
        widget=forms.DateTimeInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if description:
            return description.strip()
        return description
