from django import forms

class equipoFormulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   liga = forms.IntegerField(required=True, max_value=50000)
