# Generated by Django 4.1.1 on 2022-10-29 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('fa_id', models.IntegerField(primary_key=True, serialize=False)),
                ('fa_persona', models.CharField(max_length=30)),
                ('fa_paciente', models.CharField(max_length=30)),
                ('fa_correo', models.CharField(max_length=30)),
                ('fa_parentesco', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('me_id', models.IntegerField(primary_key=True, serialize=False)),
                ('me_especialidad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('nombre', models.CharField(max_length=30, verbose_name='Name')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('tipo_documento', models.CharField(max_length=50, verbose_name='Tipo de documento')),
                ('numero_documento', models.CharField(max_length=50, verbose_name='Numero de documento')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('ciudad', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=50, verbose_name='Telefono')),
                ('rol', models.CharField(max_length=50, verbose_name='Rol')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('pa_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pa_fecha_nacimiento', models.DateField(max_length=30)),
                ('pa_eps', models.CharField(max_length=50)),
                ('pa_rh', models.CharField(max_length=10)),
                ('pa_latitud', models.CharField(max_length=10)),
                ('pa_longitud', models.CharField(max_length=10)),
                ('pa_medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProyect.medico')),
                ('pa_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProyect.persona')),
            ],
        ),
        migrations.AddField(
            model_name='medico',
            name='me_persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProyect.persona'),
        ),
    ]
