# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlcaldiaMunicipio(models.Model):
    id_alc_mun = models.AutoField(db_column='ID_ALC_MUN', primary_key=True)  # Field name made lowercase.
    alcaldia_municipio = models.CharField(db_column='ALCALDIA_MUNICIPIO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    id_ciudad = models.ForeignKey('Ciudad', models.DO_NOTHING, db_column='ID_CIUDAD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALCALDIA_MUNICIPIO'


class Ciudad(models.Model):
    id_ciudad = models.AutoField(db_column='ID_CIUDAD', primary_key=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='CIUDAD', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CIUDAD'


class Cuestionario(models.Model):
    id_cuestionario = models.AutoField(db_column='ID_CUESTIONARIO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=200)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=500)  # Field name made lowercase.
    imagen = models.CharField(db_column='IMAGEN', max_length=200)  # Field name made lowercase.
    id_na = models.ForeignKey('NivelAcademico', models.DO_NOTHING, db_column='ID_NA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO'


class Edad(models.Model):
    id_edad = models.AutoField(db_column='ID_EDAD', primary_key=True)  # Field name made lowercase.
    rango = models.CharField(db_column='RANGO', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EDAD'


class NivelAcademico(models.Model):
    id_na = models.AutoField(db_column='ID_NA', primary_key=True)  # Field name made lowercase.
    nivel = models.CharField(db_column='NIVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NIVEL_ACADEMICO'


class Pais(models.Model):
    id_pais = models.AutoField(db_column='ID_PAIS', primary_key=True)  # Field name made lowercase.
    pais = models.CharField(db_column='PAIS', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PAIS'


class ProgramaAcademico(models.Model):
    id_pa = models.AutoField(db_column='ID_PA', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=600, blank=True, null=True)  # Field name made lowercase.
    id_ua = models.ForeignKey('UnidadAcademica', models.DO_NOTHING, db_column='ID_UA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROGRAMA_ACADEMICO'


class UnidadAcademica(models.Model):
    id_ua = models.AutoField(db_column='ID_UA', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    siglas = models.CharField(db_column='SIGLAS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    id_na = models.ForeignKey(NivelAcademico, models.DO_NOTHING, db_column='ID_NA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UNIDAD_ACADEMICA'


class Usuario(models.Model):
    id_usuario = models.AutoField(db_column='ID_USUARIO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50)  # Field name made lowercase.
    apellido1 = models.CharField(db_column='APELLIDO1', max_length=50)  # Field name made lowercase.
    apellido2 = models.CharField(db_column='APELLIDO2', max_length=50)  # Field name made lowercase.
    curp = models.CharField(db_column='CURP', max_length=50)  # Field name made lowercase.
    genero = models.CharField(db_column='GENERO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    estado_civil = models.CharField(db_column='ESTADO_CIVIL', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=50)  # Field name made lowercase.
    codigo_postal = models.CharField(db_column='CODIGO_POSTAL', max_length=10)  # Field name made lowercase.
    ciudad = models.CharField(db_column='CIUDAD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    alcaldia_municipio = models.CharField(db_column='ALCALDIA_MUNICIPIO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    id_na = models.ForeignKey(NivelAcademico, models.DO_NOTHING, db_column='ID_NA')  # Field name made lowercase.
    id_ua = models.ForeignKey(UnidadAcademica, models.DO_NOTHING, db_column='ID_UA')  # Field name made lowercase.
    id_pa = models.ForeignKey(ProgramaAcademico, models.DO_NOTHING, db_column='ID_PA')  # Field name made lowercase.
    id_edad = models.ForeignKey(Edad, models.DO_NOTHING, db_column='ID_EDAD')  # Field name made lowercase.
    id_pais_nacimiento = models.ForeignKey(Pais, models.DO_NOTHING, db_column='ID_PAIS_NACIMIENTO', related_name='usuarios_nacimiento')
    id_pais_residencia = models.ForeignKey(Pais, models.DO_NOTHING, db_column='ID_PAIS_RESIDENCIA', related_name='usuarios_residencia')

    class Meta:
        managed = False
        db_table = 'USUARIO'


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
