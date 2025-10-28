from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse # Opcional: para un mensaje de éxito simple
#from app.forms import EntrevistaForm # Importa la clase de formulario que creaste
from .models import Pacientes, EstadoPaciente  # 👈 Esto es fundamental
from .forms import PacienteForm
from app.forms import PacienteForm, EntrevistaForm

def index(request):
    return render(request, "index.html")

def base(request):
    return render(request, "base.html")

def dashboard(request):
    return render(request, 'dashboard.html')

def turnos_view(request):
    return render(request, 'turnos.html')

def entrevista_view(request):
    if request.method == 'POST':
        form = EntrevistaForm(request.POST)
        if form.is_valid():
            return redirect('gracias')  
    else:
        form = EntrevistaForm()

    return render(request, 'index.html', {'form': form})


def pacientes_list(request):
    pacientes = Pacientes.objects.all()
    return render(request, 'pacientes/pacientes_list.html', {'pacientes': pacientes})



def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pacientes_list')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/pacientes_form.html', {'form': form})


def paciente_update(request, pk):
    paciente = get_object_or_404(Pacientes, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=pacientes)
        if form.is_valid():
            form.save()
            return redirect('pacientes_list')
    else:
        form = PacienteForm(instance=pacientes)
    return render(request, 'pacientes/pacientes_form.html', {'form': form})

def paciente_delete(request, pk):
    paciente = get_object_or_404(Pacientes, dni_paciente=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('pacientes_list') 
    
    return render(request, 'pacientes/paciente_confirm_delete.html', {'pacientes': pacientes})

def estadistica_view(request):
    estados = EstadoPaciente.objects.all()
    return render(request, 'estadistica.html', {'estados': estados})   