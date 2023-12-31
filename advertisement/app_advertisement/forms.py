from django import forms
from django.forms import ModelForm
from .models import Advertisement
from django.core.exceptions import ValidationError

class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ["title", "description", "price", "auction", "image"]
        widgets = {
            "title" : forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "description" : forms.Textarea(attrs={"class": "form-control form-control-lg"}),
            "price" : forms.NumberInput(attrs={"class": "form-control form-control-lg"}),
            "auction" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "image" : forms.FileInput(attrs={"class": "form-control form-control-lg"})
        }

    def valid_title(self):
        title = self.cleaned_data.get("title")
        if title and title.startswith("?"):
            raise ValidationError("Название объявления не может начинаться с '?'.")
        return title