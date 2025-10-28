from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm

def login_view(request):
    return render(request, 'registration/login.html')

def registro_view(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return render(request, 'index.html')
        else:
            data["form"] = user_creation_form
    return render(request, 'registration/register.html', data)

