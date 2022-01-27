from cProfile import label
from logging import PlaceHolder
from django import forms

class CrearProductoForm(forms.Form):
    nombre   = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'nombre'})
    )
    precio   = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'precio'})
    )
    cantidad = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'cantidad'})
    )

    