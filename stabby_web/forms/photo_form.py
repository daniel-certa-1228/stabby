from django import forms
from ..models import Photo


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ["description", "photo", "photo_id"]
        widgets = {
            "photo": forms.ClearableFileInput(
                attrs={"class": "form-control-file", "accept": "image/*"}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.photo_id:
            self.fields["photo"].required = False
        # Add Bootstrap class to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control form-control-sm mb-2"

            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs["rows"] = 4

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if description:
            return description.strip()
        return description
