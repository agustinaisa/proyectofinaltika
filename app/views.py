from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse # Opcional: para un mensaje de éxito simple
#from app.forms import EntrevistaForm # Importa la clase de formulario que creaste
from .models import Pacientes, EstadoPaciente, Testimonio 
from .forms import PacienteForm, TestimonioForm
from app.forms import PacienteForm, EntrevistaForm
from django.contrib.auth.decorators import user_passes_test

def index(request):
    testimonios = Testimonio.objects.filter(publicado=True).order_by('-fecha_envio')[:10] 
    return render(request, "index.html", {'testimonios': testimonios})

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
        form = PacienteForm(request.POST, instance=paciente) 
        if form.is_valid():
            form.save()
            return redirect('pacientes_list')
    else:
        form = PacienteForm(instance=paciente) 
    return render(request, 'pacientes/pacientes_form.html', {'form': form})

def paciente_delete(request, pk):
    paciente = get_object_or_404(Pacientes, dni_paciente=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('pacientes_list') 
    return render(request, 'pacientes/paciente_confirm_delete.html', {'paciente': paciente})

def estadistica_view(request):
    estados = EstadoPaciente.objects.all()
    return render(request, 'estadistica.html', {'estados': estados})   

def comprobantes_view(request):
    return render(request, 'comprobantes.html')

def enviar_testimonio(request):
    if request.method == 'POST':
        form = TestimonioForm(request.POST)
        if form.is_valid():
            testimonio = form.save(commit=False)
            testimonio.usuario = request.user if request.user.is_authenticated else None
            testimonio.save()
            return redirect('index')
    else:
        form = TestimonioForm()
    return render(request, 'testimonio/enviar_testimonio.html', {'form': form})

# Mostrar testimonios públicos (aprobados)
def testimonios_publicos(request):
    testimonios = Testimonio.objects.filter(estado='aprobado', publicado=True).order_by('-fecha_envio')
    return render(request, 'testimonios_publicos.html', {'testimonios': testimonios})


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def testimonios_lista(request):
    testimonios = Testimonio.objects.all().order_by('-fecha_envio')
    return render(request, 'dashboard/testimonios.html', {'testimonios': testimonios})
# Acciones del admin 
def aprobar_testimonio(request, id):
    testimonio = get_object_or_404(Testimonio, id=id)
    testimonio.estado = 'aprobado'
    testimonio.publicado = True
    testimonio.save()
    return redirect('testimonios_lista')

def restringir_testimonio(request, id):
    testimonio = get_object_or_404(Testimonio, id=id)
    testimonio.estado = 'restringido'
    testimonio.publicado = False
    testimonio.save()
    return redirect('testimonios_lista')
def testimonios_inicio(request):
    testimonios = Testimonio.objects.filter(publicado=True).order_by('-fecha_envio')
    return render(request, 'testimonio/test_public.html', {'testimonios': testimonios})

def eliminar_testimonio(request, id):
    testimonio = get_object_or_404(Testimonio, id=id)
    testimonio.delete()
    return redirect('testimonios_lista')