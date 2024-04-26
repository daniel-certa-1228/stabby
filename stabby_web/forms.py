from django import forms
from .models import Blade, Knife, Sharpener, WorkLog


class BladeForm(forms.ModelForm):

    class Meta:
        model = Blade
        exclude = ["create_date", "edit_date", "is_active"]


class KnifeForm(forms.ModelForm):

    class Meta:
        model = Knife
        exclude = ["create_date", "edit_date", "is_active", "user"]


class SharpenerForm(forms.ModelForm):

    class Meta:
        model = Sharpener
        exclude = ["create_date", "edit_date", "is_active", "user"]


class WorkLogForm(forms.ModelForm):

    class Meta:
        model = WorkLog
        exclude = ["create_date", "edit_date", "is_active"]
