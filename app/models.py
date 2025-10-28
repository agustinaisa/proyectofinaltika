# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Centrosterapeuticos(models.Model):
    id_centroterapeutico = models.IntegerField(db_column='ID_CentroTerapeutico', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'centrosterapeuticos'


class Detallepagos(models.Model):
    codigo_pago = models.IntegerField(db_column='Codigo_Pago', primary_key=True)  # Field name made lowercase.
    monto = models.DecimalField(db_column='Monto', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detallepagos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Especialidades(models.Model):
    id_especialidades = models.IntegerField(db_column='id_Especialidades', primary_key=True)  # Field name made lowercase.
    id_especialista = models.IntegerField()
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    matricula = models.IntegerField(db_column='Matricula', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'especialidades'


class Especialistas(models.Model):
    id_especialistas = models.IntegerField(db_column='ID_Especialistas', primary_key=True)  # Field name made lowercase.
    id_especialidad_especialista = models.CharField(max_length=45, blank=True, null=True)
    dni = models.IntegerField(db_column='DNI', blank=True, null=True)  # Field name made lowercase.
    matricula = models.IntegerField(db_column='Matricula', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'especialistas'


class HistorialPaciente(models.Model):
    nro_historia_paciente = models.IntegerField(db_column='Nro_Historia_paciente', primary_key=True)  # Field name made lowercase.
    antecedentes = models.CharField(db_column='Antecedentes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'historial_paciente'


class Horariosespecialistas(models.Model):
    id_horariosespecialistas = models.IntegerField(db_column='ID_HorariosEspecialistas', primary_key=True)  # Field name made lowercase.
    id_especialistas = models.CharField(max_length=100, blank=True, null=True)
    horarioinicio = models.TimeField(db_column='HorarioInicio', blank=True, null=True)  # Field name made lowercase.
    horariofin = models.TimeField(db_column='HorarioFin', blank=True, null=True)  # Field name made lowercase.
    id_especialista = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horariosespecialistas'


class ObrasSociales(models.Model):
    id_os = models.IntegerField(db_column='ID_OS', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'obras_sociales'


class Pacientes(models.Model):
    dni_paciente = models.IntegerField(db_column='DNI_paciente', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)
    apellido = models.CharField(db_column='Apellido', max_length=45, blank=True, null=True)
    fecha_nacimiento = models.DateField(db_column='Fecha_Nacimiento', blank=True, null=True)
    sexo = models.CharField(db_column='Sexo', max_length=45, blank=True, null=True)
    telefono = models.IntegerField(db_column='Telefono', blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'pacientes'  

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class EstadoPaciente(models.Model):
    paciente = models.OneToOneField(Pacientes, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

def __str__(self):
    return f"{self.paciente} - {'Activo' if self.activo else 'Dado de baja'}"



class Pagos(models.Model):
    nro_pago = models.IntegerField(db_column='Nro_Pago', primary_key=True)  # Field name made lowercase.
    monto = models.DecimalField(db_column='Monto', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    descuentos = models.DecimalField(db_column='Descuentos', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    forma_pago = models.CharField(db_column='Forma_Pago', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fecha_pago = models.DateField(db_column='Fecha_Pago', blank=True, null=True)  # Field name made lowercase.
    estado_pago = models.CharField(db_column='Estado_Pago', max_length=45, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pagos'


class Turnos(models.Model):
    nro_turno = models.IntegerField(db_column='Nro_Turno', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turnos'

class Entrevista(models.Model):
    fecha = models.DateField()
    observaciones = models.TextField(blank=True, null=True)
    pacientes = models.ForeignKey(Pacientes, on_delete=models.CASCADE)

    class Meta:
        db_table = 'entrevista'
