from django import forms
from stabby_web.services.dropdown_service import DropdownService
from ..models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["brand", "description", "photo", "photo_id"]
        widgets = {
            "photo": forms.ClearableFileInput(
                attrs={"class": "form-control-file", "accept": "image/*"}
            )
        }

    def __init__(self, *args, **kwargs):
        active = kwargs.pop("active", None)  # Extract 'active' from kwargs
        super().__init__(*args, **kwargs)

        # Conditionally set 'brand' as required if 'active' is 'library'
        if active == "library":
            self.fields["brand"].required = True
        else:
            self.fields["brand"].required = False

        # Bootstrap styling and other initializations
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control form-control-sm mb-2"
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs["rows"] = 4

        # Dropdown queryset for brand
        self.fields["brand"].queryset = DropdownService.get_brands()
        self.fields["brand"].empty_label = "Select Brand"
