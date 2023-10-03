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


class CuestionarioTransversal(models.Model):
    id_cuestionario_transversal = models.AutoField(db_column='ID_CUESTIONARIO_TRANSVERSAL', primary_key=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='ID_USUARIO')  # Field name made lowercase.
    pregunta_1 = models.CharField(db_column='PREGUNTA_1', max_length=200)  # Field name made lowercase.
    pregunta_2 = models.CharField(db_column='PREGUNTA_2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pregunta_3 = models.CharField(db_column='PREGUNTA_3', max_length=200)  # Field name made lowercase.
    pregunta_4 = models.CharField(db_column='PREGUNTA_4', max_length=200)  # Field name made lowercase.
    pregunta_5 = models.CharField(db_column='PREGUNTA_5', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pregunta_6 = models.CharField(db_column='PREGUNTA_6', max_length=200)  # Field name made lowercase.
    pregunta_7 = models.CharField(db_column='PREGUNTA_7', max_length=200)  # Field name made lowercase.
    pregunta_8 = models.CharField(db_column='PREGUNTA_8', max_length=200)  # Field name made lowercase.
    pregunta_9 = models.CharField(db_column='PREGUNTA_9', max_length=200)  # Field name made lowercase.
    pregunta_10 = models.CharField(db_column='PREGUNTA_10', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pregunta_11 = models.CharField(db_column='PREGUNTA_11', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pregunta_12 = models.CharField(db_column='PREGUNTA_12', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pregunta_13 = models.CharField(db_column='PREGUNTA_13', max_length=200)  # Field name made lowercase.
    pregunta_14 = models.CharField(db_column='PREGUNTA_14', max_length=200)  # Field name made lowercase.
    pregunta_15 = models.CharField(db_column='PREGUNTA_15', max_length=200)  # Field name made lowercase.
    pregunta_16 = models.CharField(db_column='PREGUNTA_16', max_length=200)  # Field name made lowercase.
    pregunta_17 = models.CharField(db_column='PREGUNTA_17', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pregunta_18 = models.CharField(db_column='PREGUNTA_18', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pregunta_19 = models.CharField(db_column='PREGUNTA_19', max_length=200)  # Field name made lowercase.
    pregunta_20 = models.CharField(db_column='PREGUNTA_20', max_length=200)  # Field name made lowercase.
    pregunta_21 = models.CharField(db_column='PREGUNTA_21', max_length=200)  # Field name made lowercase.
    pregunta_22 = models.CharField(db_column='PREGUNTA_22', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pregunta_23 = models.CharField(db_column='PREGUNTA_23', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pregunta_24 = models.CharField(db_column='PREGUNTA_24', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pregunta_25 = models.CharField(db_column='PREGUNTA_25', max_length=100)  # Field name made lowercase.
    pregunta_26 = models.CharField(db_column='PREGUNTA_26', max_length=100)  # Field name made lowercase.
    pregunta_27 = models.CharField(db_column='PREGUNTA_27', max_length=100)  # Field name made lowercase.
    pregunta_28 = models.CharField(db_column='PREGUNTA_28', max_length=100)  # Field name made lowercase.
    pregunta_29 = models.CharField(db_column='PREGUNTA_29', max_length=100)  # Field name made lowercase.
    pregunta_30 = models.CharField(db_column='PREGUNTA_30', max_length=100)  # Field name made lowercase.
    pregunta_31 = models.CharField(db_column='PREGUNTA_31', max_length=100)  # Field name made lowercase.
    pregunta_32 = models.CharField(db_column='PREGUNTA_32', max_length=100)  # Field name made lowercase.
    pregunta_33 = models.CharField(db_column='PREGUNTA_33', max_length=100)  # Field name made lowercase.
    pregunta_34 = models.CharField(db_column='PREGUNTA_34', max_length=100)  # Field name made lowercase.
    pregunta_35 = models.CharField(db_column='PREGUNTA_35', max_length=100)  # Field name made lowercase.
    pregunta_36 = models.CharField(db_column='PREGUNTA_36', max_length=100)  # Field name made lowercase.
    pregunta_37 = models.CharField(db_column='PREGUNTA_37', max_length=100)  # Field name made lowercase.
    pregunta_38 = models.CharField(db_column='PREGUNTA_38', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSVERSAL'


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
    codigo_postal = models.CharField(db_column='CODIGO_POSTAL', max_length=10, blank=True, null=True)  # Field name made lowercase.
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
