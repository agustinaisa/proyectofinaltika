from django.shortcuts import render, redirect 
# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Pacientes
from .models import Entrevista
from .models import Testimonio

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['dni_paciente', 'nombre', 'apellido', 'fecha_nacimiento', 'sexo', 'telefono', 'email']

class EntrevistaForm(forms.ModelForm):
    class Meta:
        model = Entrevista
        fields = '__all__'

class TestimonioForm(forms.ModelForm):
    class Meta:
        model = Testimonio
        fields = ['relacion','titulo', 'contenido', 'imagen']
        widgets = {
            'relacion': forms.TextInput(attrs={
                'placeholder': 'Ejemplo: Mamá de Mateo, Papá de Lucía, Tutor de Ana...',
                'class': 'form-control'
            }),
            'contenido': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        }