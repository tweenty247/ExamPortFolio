from django import forms
from .models import DataName


class ModelDataName(forms.ModelForm):
    class Meta:
        model = DataName
        fields = '__all__'



