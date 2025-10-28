from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class CustomUserCreationForm(UserCreationForm):
    #email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    #def clean_email(self):
    #  if User.objects.filter(email=email).exists():
    #        raise forms.ValidationError("Este correo electrónico ya está en uso.")
    #    return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        grupo_usuarios, created = Group.objects.get_or_create(name='Usuarios')
        user.groups.add(grupo_usuarios)
        return user