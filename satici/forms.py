from django import forms
from .models import Satici

class SaticiForm(forms.ModelForm):
    class Meta:
        model = Satici
        fields = [ 'img','header','text' ]
       