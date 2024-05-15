from django import forms
from ..models import WorkLog


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
