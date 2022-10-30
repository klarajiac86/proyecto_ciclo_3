from django.db import models


class Persona(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length=20, unique=True)
    password = models.CharField('Password', max_length=256)
    nombre = models.CharField('Name', max_length=30)
    apellido = models.CharField('Apellido', max_length=30)
    email = models.EmailField('Email', max_length=100)
    tipo_documento = models.CharField('Tipo de documento', max_length=50)
    numero_documento = models.CharField('Numero de documento', max_length=50)
    direccion = models.CharField('Direccion', max_length=100)
    ciudad = models.CharField(max_length=30)
    telefono = models.CharField('Telefono', max_length=50)
    rol = models.CharField('Rol', max_length=50)


class Medico(models.Model):
    me_id = models.IntegerField(primary_key=True)
    me_persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    me_especialidad = models.CharField(max_length=30)


class Paciente(models.Model):
    pa_id = models.IntegerField(primary_key=True)
    pa_persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    pa_fecha_nacimiento = models.DateField(max_length=30)
    pa_eps = models.CharField(max_length=50)
    pa_rh = models.CharField(max_length=10)
    pa_latitud = models.CharField(max_length=10)
    pa_longitud = models.CharField(max_length=10)
    pa_medico = models.ForeignKey(Medico, null=False, on_delete=models.CASCADE)


class Familiar(models.Model):
    fa_id = models.IntegerField(primary_key=True)
    fa_persona = models.CharField(max_length=30)
    fa_paciente = models.CharField(max_length=30)
    fa_correo = models.CharField(max_length=30)
    fa_parentesco = models.CharField(max_length=30)
