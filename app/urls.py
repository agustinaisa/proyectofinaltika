from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),

    path("dashboard/", views.dashboard, name="dashboard"),
    path("base/", views.base, name="base"),
    path("entrevista/", views.entrevista_view, name="entrevista"),
    path("turnos/", views.turnos_view, name="turnos"),
    path("estadistica/", views.estadistica_view, name="estadistica"),
    # CRUD Pacientes
    path("pacientes/", views.pacientes_list, name="pacientes_list"),
    path("pacientes/nuevo/", views.paciente_create, name="pacientes_create"),
    path("pacientes/editar/<int:pk>/", views.paciente_update, name="pacientes_update"),
    path("pacientes/eliminar/<int:pk>/", views.paciente_delete, name="pacientes_delete"),
]
