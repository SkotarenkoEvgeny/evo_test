from django import forms

from .models import SimpleName


class NameForm(forms.ModelForm):
    class Meta:
        model = SimpleName
        fields = ('name',)
