# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CuestionarioEmpleadores(models.Model):
    id_cuestionario = models.AutoField(db_column='ID_CUESTIONARIO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='ID_USUARIO')  # Field name made lowercase.
    pregunta_1 = models.ForeignKey('CuestionarioEmpleadoresPregunta1', models.DO_NOTHING, db_column='PREGUNTA_1')  # Field name made lowercase.
    pregunta_2 = models.ForeignKey('CuestionarioEmpleadoresPregunta2', models.DO_NOTHING, db_column='PREGUNTA_2')  # Field name made lowercase.
    pregunta_3 = models.ForeignKey('CuestionarioEmpleadoresPregunta3', models.DO_NOTHING, db_column='PREGUNTA_3')  # Field name made lowercase.
    pregunta_4 = models.PositiveIntegerField(db_column='PREGUNTA_4', blank=True, null=True)  # Field name made lowercase.
    pregunta_5 = models.CharField(db_column='PREGUNTA_5', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pregunta_6 = models.PositiveIntegerField(db_column='PREGUNTA_6', blank=True, null=True)  # Field name made lowercase.
    pregunta_7 = models.ForeignKey('CuestionarioEmpleadoresPregunta7', models.DO_NOTHING, db_column='PREGUNTA_7')  # Field name made lowercase.
    pregunta_8 = models.ForeignKey('CuestionarioEmpleadoresPregunta8', models.DO_NOTHING, db_column='PREGUNTA_8')  # Field name made lowercase.
    pregunta_9 = models.ForeignKey('CuestionarioEmpleadoresPregunta9', models.DO_NOTHING, db_column='PREGUNTA_9')  # Field name made lowercase.
    pregunta_10 = models.ForeignKey('CuestionarioEmpleadoresPregunta10', models.DO_NOTHING, db_column='PREGUNTA_10')  # Field name made lowercase.
    pregunta_11 = models.ForeignKey('CuestionarioEmpleadoresPregunta11', models.DO_NOTHING, db_column='PREGUNTA_11')  # Field name made lowercase.
    pregunta_12 = models.ForeignKey('CuestionarioEmpleadoresPregunta12', models.DO_NOTHING, db_column='PREGUNTA_12')  # Field name made lowercase.
    pregunta_13 = models.ForeignKey('CuestionarioEmpleadoresPregunta13', models.DO_NOTHING, db_column='PREGUNTA_13')  # Field name made lowercase.
    pregunta_14 = models.ForeignKey('CuestionarioEmpleadoresPregunta14', models.DO_NOTHING, db_column='PREGUNTA_14')  # Field name made lowercase.
    pregunta_15 = models.ForeignKey('CuestionarioEmpleadoresPregunta15', models.DO_NOTHING, db_column='PREGUNTA_15')  # Field name made lowercase.
    pregunta_16 = models.ForeignKey('CuestionarioEmpleadoresPregunta16', models.DO_NOTHING, db_column='PREGUNTA_16')  # Field name made lowercase.
    pregunta_17 = models.ForeignKey('CuestionarioEmpleadoresPregunta17', models.DO_NOTHING, db_column='PREGUNTA_17')  # Field name made lowercase.
    pregunta_18 = models.ForeignKey('CuestionarioEmpleadoresPregunta18', models.DO_NOTHING, db_column='PREGUNTA_18')  # Field name made lowercase.
    pregunta_19 = models.ForeignKey('CuestionarioEmpleadoresPregunta19', models.DO_NOTHING, db_column='PREGUNTA_19')  # Field name made lowercase.
    pregunta_20 = models.ForeignKey('CuestionarioEmpleadoresPregunta20', models.DO_NOTHING, db_column='PREGUNTA_20')  # Field name made lowercase.
    pregunta_21 = models.ForeignKey('CuestionarioEmpleadoresPregunta21', models.DO_NOTHING, db_column='PREGUNTA_21')  # Field name made lowercase.
    pregunta_22 = models.ForeignKey('CuestionarioEmpleadoresPregunta22', models.DO_NOTHING, db_column='PREGUNTA_22')  # Field name made lowercase.
    pregunta_23 = models.ForeignKey('CuestionarioEmpleadoresPregunta23', models.DO_NOTHING, db_column='PREGUNTA_23')  # Field name made lowercase.
    pregunta_24 = models.ForeignKey('CuestionarioEmpleadoresPregunta24', models.DO_NOTHING, db_column='PREGUNTA_24')  # Field name made lowercase.
    pregunta_25 = models.ForeignKey('CuestionarioEmpleadoresPregunta25', models.DO_NOTHING, db_column='PREGUNTA_25')  # Field name made lowercase.
    pregunta_26 = models.ForeignKey('CuestionarioEmpleadoresPregunta26', models.DO_NOTHING, db_column='PREGUNTA_26')  # Field name made lowercase.
    pregunta_27 = models.ForeignKey('CuestionarioEmpleadoresPregunta27', models.DO_NOTHING, db_column='PREGUNTA_27')  # Field name made lowercase.
    pregunta_28 = models.ForeignKey('CuestionarioEmpleadoresPregunta28', models.DO_NOTHING, db_column='PREGUNTA_28')  # Field name made lowercase.
    pregunta_29 = models.ForeignKey('CuestionarioEmpleadoresPregunta29', models.DO_NOTHING, db_column='PREGUNTA_29')  # Field name made lowercase.
    pregunta_30 = models.ForeignKey('CuestionarioEmpleadoresPregunta30', models.DO_NOTHING, db_column='PREGUNTA_30')  # Field name made lowercase.
    pregunta_31 = models.ForeignKey('CuestionarioEmpleadoresPregunta31', models.DO_NOTHING, db_column='PREGUNTA_31')  # Field name made lowercase.
    pregunta_32 = models.ForeignKey('CuestionarioEmpleadoresPregunta32', models.DO_NOTHING, db_column='PREGUNTA_32')  # Field name made lowercase.
    pregunta_33 = models.ForeignKey('CuestionarioEmpleadoresPregunta33', models.DO_NOTHING, db_column='PREGUNTA_33')  # Field name made lowercase.
    pregunta_34 = models.ForeignKey('CuestionarioEmpleadoresPregunta34', models.DO_NOTHING, db_column='PREGUNTA_34')  # Field name made lowercase.
    pregunta_35 = models.ForeignKey('CuestionarioEmpleadoresPregunta35', models.DO_NOTHING, db_column='PREGUNTA_35')  # Field name made lowercase.
    pregunta_36 = models.ForeignKey('CuestionarioEmpleadoresPregunta36', models.DO_NOTHING, db_column='PREGUNTA_36')  # Field name made lowercase.
    pregunta_37 = models.ForeignKey('CuestionarioEmpleadoresPregunta37', models.DO_NOTHING, db_column='PREGUNTA_37')  # Field name made lowercase.
    pregunta_38 = models.IntegerField(db_column='PREGUNTA_38', blank=True, null=True)  # Field name made lowercase.
    pregunta_39 = models.IntegerField(db_column='PREGUNTA_39', blank=True, null=True)  # Field name made lowercase.
    pregunta_40 = models.IntegerField(db_column='PREGUNTA_40', blank=True, null=True)  # Field name made lowercase.
    pregunta_41 = models.IntegerField(db_column='PREGUNTA_41', blank=True, null=True)  # Field name made lowercase.
    pregunta_42 = models.IntegerField(db_column='PREGUNTA_42', blank=True, null=True)  # Field name made lowercase.
    pregunta_43 = models.IntegerField(db_column='PREGUNTA_43', blank=True, null=True)  # Field name made lowercase.
    pregunta_44 = models.IntegerField(db_column='PREGUNTA_44', blank=True, null=True)  # Field name made lowercase.
    pregunta_45 = models.IntegerField(db_column='PREGUNTA_45', blank=True, null=True)  # Field name made lowercase.
    pregunta_46 = models.IntegerField(db_column='PREGUNTA_46', blank=True, null=True)  # Field name made lowercase.
    pregunta_47 = models.IntegerField(db_column='PREGUNTA_47', blank=True, null=True)  # Field name made lowercase.
    pregunta_48 = models.ForeignKey('CuestionarioEmpleadoresPregunta48', models.DO_NOTHING, db_column='PREGUNTA_48')  # Field name made lowercase.
    pregunta_49 = models.ForeignKey('CuestionarioEmpleadoresPregunta49', models.DO_NOTHING, db_column='PREGUNTA_49')  # Field name made lowercase.
    pregunta_50 = models.ForeignKey('CuestionarioEmpleadoresPregunta50', models.DO_NOTHING, db_column='PREGUNTA_50')  # Field name made lowercase.
    pregunta_51 = models.ForeignKey('CuestionarioEmpleadoresPregunta51', models.DO_NOTHING, db_column='PREGUNTA_51')  # Field name made lowercase.
    pregunta_52 = models.ForeignKey('CuestionarioEmpleadoresPregunta52', models.DO_NOTHING, db_column='PREGUNTA_52')  # Field name made lowercase.
    pregunta_53 = models.ForeignKey('CuestionarioEmpleadoresPregunta53', models.DO_NOTHING, db_column='PREGUNTA_53')  # Field name made lowercase.
    pregunta_54 = models.ForeignKey('CuestionarioEmpleadoresPregunta54', models.DO_NOTHING, db_column='PREGUNTA_54')  # Field name made lowercase.
    pregunta_55 = models.ForeignKey('CuestionarioEmpleadoresPregunta55', models.DO_NOTHING, db_column='PREGUNTA_55')  # Field name made lowercase.
    pregunta_56 = models.ForeignKey('CuestionarioEmpleadoresPregunta56', models.DO_NOTHING, db_column='PREGUNTA_56')  # Field name made lowercase.
    pregunta_57 = models.ForeignKey('CuestionarioEmpleadoresPregunta57', models.DO_NOTHING, db_column='PREGUNTA_57')  # Field name made lowercase.
    pregunta_58 = models.ForeignKey('CuestionarioEmpleadoresPregunta58', models.DO_NOTHING, db_column='PREGUNTA_58')  # Field name made lowercase.
    pregunta_59 = models.ForeignKey('CuestionarioEmpleadoresPregunta59', models.DO_NOTHING, db_column='PREGUNTA_59')  # Field name made lowercase.
    pregunta_60 = models.PositiveIntegerField(db_column='PREGUNTA_60')  # Field name made lowercase.
    pregunta_61 = models.PositiveIntegerField(db_column='PREGUNTA_61')  # Field name made lowercase.
    pregunta_62 = models.ForeignKey('CuestionarioEmpleadoresPregunta62', models.DO_NOTHING, db_column='PREGUNTA_62')  # Field name made lowercase.
    pregunta_63 = models.ForeignKey('CuestionarioEmpleadoresPregunta63', models.DO_NOTHING, db_column='PREGUNTA_63')  # Field name made lowercase.
    pregunta_64 = models.ForeignKey('CuestionarioEmpleadoresPregunta64', models.DO_NOTHING, db_column='PREGUNTA_64')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES'


class CuestionarioEmpleadoresPregunta1(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_1'


class CuestionarioEmpleadoresPregunta10(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_10'


class CuestionarioEmpleadoresPregunta11(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_11'


class CuestionarioEmpleadoresPregunta12(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_12'


class CuestionarioEmpleadoresPregunta13(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_13'


class CuestionarioEmpleadoresPregunta14(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_14'


class CuestionarioEmpleadoresPregunta15(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_15'


class CuestionarioEmpleadoresPregunta16(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_16'


class CuestionarioEmpleadoresPregunta17(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_17'


class CuestionarioEmpleadoresPregunta18(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_18'


class CuestionarioEmpleadoresPregunta19(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_19'


class CuestionarioEmpleadoresPregunta2(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_2'


class CuestionarioEmpleadoresPregunta20(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_20'


class CuestionarioEmpleadoresPregunta21(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_21'


class CuestionarioEmpleadoresPregunta22(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_22'


class CuestionarioEmpleadoresPregunta23(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_23'


class CuestionarioEmpleadoresPregunta24(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_24'


class CuestionarioEmpleadoresPregunta25(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_25'


class CuestionarioEmpleadoresPregunta26(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_26'


class CuestionarioEmpleadoresPregunta27(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_27'


class CuestionarioEmpleadoresPregunta28(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_28'


class CuestionarioEmpleadoresPregunta29(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_29'


class CuestionarioEmpleadoresPregunta3(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_3'


class CuestionarioEmpleadoresPregunta30(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_30'


class CuestionarioEmpleadoresPregunta31(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_31'


class CuestionarioEmpleadoresPregunta32(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_32'


class CuestionarioEmpleadoresPregunta33(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_33'


class CuestionarioEmpleadoresPregunta34(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_34'


class CuestionarioEmpleadoresPregunta35(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_35'


class CuestionarioEmpleadoresPregunta36(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_36'


class CuestionarioEmpleadoresPregunta37(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_37'


class CuestionarioEmpleadoresPregunta48(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_48'


class CuestionarioEmpleadoresPregunta49(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_49'


class CuestionarioEmpleadoresPregunta50(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_50'


class CuestionarioEmpleadoresPregunta51(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_51'


class CuestionarioEmpleadoresPregunta52(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_52'


class CuestionarioEmpleadoresPregunta53(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_53'


class CuestionarioEmpleadoresPregunta54(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_54'


class CuestionarioEmpleadoresPregunta55(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_55'


class CuestionarioEmpleadoresPregunta56(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_56'


class CuestionarioEmpleadoresPregunta57(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_57'


class CuestionarioEmpleadoresPregunta58(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_58'


class CuestionarioEmpleadoresPregunta59(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_59'


class CuestionarioEmpleadoresPregunta62(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_62'


class CuestionarioEmpleadoresPregunta63(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_63'


class CuestionarioEmpleadoresPregunta64(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_64'


class CuestionarioEmpleadoresPregunta7(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_7'


class CuestionarioEmpleadoresPregunta8(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_8'


class CuestionarioEmpleadoresPregunta9(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_EMPLEADORES_PREGUNTA_9'


class CuestionarioTransevrsalPregunta1(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_1'


class CuestionarioTransevrsalPregunta10(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_10'


class CuestionarioTransevrsalPregunta11(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_11'


class CuestionarioTransevrsalPregunta12(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_12'


class CuestionarioTransevrsalPregunta15(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_15'


class CuestionarioTransevrsalPregunta16(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_16'


class CuestionarioTransevrsalPregunta17(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_17'


class CuestionarioTransevrsalPregunta18(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_18'


class CuestionarioTransevrsalPregunta19(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_19'


class CuestionarioTransevrsalPregunta2(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_2'


class CuestionarioTransevrsalPregunta20(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_20'


class CuestionarioTransevrsalPregunta21(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_21'


class CuestionarioTransevrsalPregunta22(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_22'


class CuestionarioTransevrsalPregunta23(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_23'


class CuestionarioTransevrsalPregunta24(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_24'


class CuestionarioTransevrsalPregunta25(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_25'


class CuestionarioTransevrsalPregunta26(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_26'


class CuestionarioTransevrsalPregunta27(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_27'


class CuestionarioTransevrsalPregunta28(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_28'


class CuestionarioTransevrsalPregunta29(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_29'


class CuestionarioTransevrsalPregunta3(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_3'


class CuestionarioTransevrsalPregunta30(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_30'


class CuestionarioTransevrsalPregunta31(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_31'


class CuestionarioTransevrsalPregunta32(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_32'


class CuestionarioTransevrsalPregunta33(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_33'


class CuestionarioTransevrsalPregunta34(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_34'


class CuestionarioTransevrsalPregunta35(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_35'


class CuestionarioTransevrsalPregunta36(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_36'


class CuestionarioTransevrsalPregunta37(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_37'


class CuestionarioTransevrsalPregunta38(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_38'


class CuestionarioTransevrsalPregunta39(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_39'


class CuestionarioTransevrsalPregunta4(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_4'


class CuestionarioTransevrsalPregunta5(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_5'


class CuestionarioTransevrsalPregunta6(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_6'


class CuestionarioTransevrsalPregunta7(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_7'


class CuestionarioTransevrsalPregunta8(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_8'


class CuestionarioTransevrsalPregunta9(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSEVRSAL_PREGUNTA_9'


class CuestionarioTransversal(models.Model):
    id_cuestionario = models.AutoField(db_column='ID_CUESTIONARIO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='ID_USUARIO')  # Field name made lowercase.
    pregunta_1 = models.ForeignKey(CuestionarioTransevrsalPregunta1, models.DO_NOTHING, db_column='PREGUNTA_1')  # Field name made lowercase.
    pregunta_2 = models.ForeignKey(CuestionarioTransevrsalPregunta2, models.DO_NOTHING, db_column='PREGUNTA_2')  # Field name made lowercase.
    pregunta_3 = models.ForeignKey(CuestionarioTransevrsalPregunta3, models.DO_NOTHING, db_column='PREGUNTA_3')  # Field name made lowercase.
    pregunta_4 = models.ForeignKey(CuestionarioTransevrsalPregunta4, models.DO_NOTHING, db_column='PREGUNTA_4')  # Field name made lowercase.
    pregunta_5 = models.ForeignKey(CuestionarioTransevrsalPregunta5, models.DO_NOTHING, db_column='PREGUNTA_5')  # Field name made lowercase.
    pregunta_6 = models.ForeignKey(CuestionarioTransevrsalPregunta6, models.DO_NOTHING, db_column='PREGUNTA_6')  # Field name made lowercase.
    pregunta_7 = models.ForeignKey(CuestionarioTransevrsalPregunta7, models.DO_NOTHING, db_column='PREGUNTA_7')  # Field name made lowercase.
    pregunta_8 = models.ForeignKey(CuestionarioTransevrsalPregunta8, models.DO_NOTHING, db_column='PREGUNTA_8')  # Field name made lowercase.
    pregunta_9 = models.ForeignKey(CuestionarioTransevrsalPregunta9, models.DO_NOTHING, db_column='PREGUNTA_9')  # Field name made lowercase.
    pregunta_10 = models.ForeignKey(CuestionarioTransevrsalPregunta10, models.DO_NOTHING, db_column='PREGUNTA_10')  # Field name made lowercase.
    pregunta_11 = models.ForeignKey(CuestionarioTransevrsalPregunta11, models.DO_NOTHING, db_column='PREGUNTA_11')  # Field name made lowercase.
    pregunta_12 = models.ForeignKey(CuestionarioTransevrsalPregunta12, models.DO_NOTHING, db_column='PREGUNTA_12')  # Field name made lowercase.
    pregunta_13 = models.CharField(db_column='PREGUNTA_13', max_length=500)  # Field name made lowercase.
    pregunta_14 = models.CharField(db_column='PREGUNTA_14', max_length=500)  # Field name made lowercase.
    pregunta_15 = models.ForeignKey(CuestionarioTransevrsalPregunta15, models.DO_NOTHING, db_column='PREGUNTA_15')  # Field name made lowercase.
    pregunta_16 = models.ForeignKey(CuestionarioTransevrsalPregunta16, models.DO_NOTHING, db_column='PREGUNTA_16')  # Field name made lowercase.
    pregunta_17 = models.ForeignKey(CuestionarioTransevrsalPregunta17, models.DO_NOTHING, db_column='PREGUNTA_17')  # Field name made lowercase.
    pregunta_18 = models.ForeignKey(CuestionarioTransevrsalPregunta18, models.DO_NOTHING, db_column='PREGUNTA_18')  # Field name made lowercase.
    pregunta_19 = models.ForeignKey(CuestionarioTransevrsalPregunta19, models.DO_NOTHING, db_column='PREGUNTA_19')  # Field name made lowercase.
    pregunta_20 = models.ForeignKey(CuestionarioTransevrsalPregunta20, models.DO_NOTHING, db_column='PREGUNTA_20')  # Field name made lowercase.
    pregunta_21 = models.ForeignKey(CuestionarioTransevrsalPregunta21, models.DO_NOTHING, db_column='PREGUNTA_21')  # Field name made lowercase.
    pregunta_22 = models.ForeignKey(CuestionarioTransevrsalPregunta22, models.DO_NOTHING, db_column='PREGUNTA_22')  # Field name made lowercase.
    pregunta_23 = models.ForeignKey(CuestionarioTransevrsalPregunta23, models.DO_NOTHING, db_column='PREGUNTA_23')  # Field name made lowercase.
    pregunta_24 = models.ForeignKey(CuestionarioTransevrsalPregunta24, models.DO_NOTHING, db_column='PREGUNTA_24')  # Field name made lowercase.
    pregunta_25 = models.ForeignKey(CuestionarioTransevrsalPregunta25, models.DO_NOTHING, db_column='PREGUNTA_25')  # Field name made lowercase.
    pregunta_26 = models.ForeignKey(CuestionarioTransevrsalPregunta26, models.DO_NOTHING, db_column='PREGUNTA_26')  # Field name made lowercase.
    pregunta_27 = models.ForeignKey(CuestionarioTransevrsalPregunta27, models.DO_NOTHING, db_column='PREGUNTA_27')  # Field name made lowercase.
    pregunta_28 = models.ForeignKey(CuestionarioTransevrsalPregunta28, models.DO_NOTHING, db_column='PREGUNTA_28')  # Field name made lowercase.
    pregunta_29 = models.ForeignKey(CuestionarioTransevrsalPregunta29, models.DO_NOTHING, db_column='PREGUNTA_29')  # Field name made lowercase.
    pregunta_30 = models.ForeignKey(CuestionarioTransevrsalPregunta30, models.DO_NOTHING, db_column='PREGUNTA_30')  # Field name made lowercase.
    pregunta_31 = models.ForeignKey(CuestionarioTransevrsalPregunta31, models.DO_NOTHING, db_column='PREGUNTA_31')  # Field name made lowercase.
    pregunta_32 = models.ForeignKey(CuestionarioTransevrsalPregunta32, models.DO_NOTHING, db_column='PREGUNTA_32')  # Field name made lowercase.
    pregunta_33 = models.ForeignKey(CuestionarioTransevrsalPregunta33, models.DO_NOTHING, db_column='PREGUNTA_33')  # Field name made lowercase.
    pregunta_34 = models.ForeignKey(CuestionarioTransevrsalPregunta34, models.DO_NOTHING, db_column='PREGUNTA_34')  # Field name made lowercase.
    pregunta_35 = models.ForeignKey(CuestionarioTransevrsalPregunta35, models.DO_NOTHING, db_column='PREGUNTA_35')  # Field name made lowercase.
    pregunta_36 = models.ForeignKey(CuestionarioTransevrsalPregunta36, models.DO_NOTHING, db_column='PREGUNTA_36')  # Field name made lowercase.
    pregunta_37 = models.ForeignKey(CuestionarioTransevrsalPregunta37, models.DO_NOTHING, db_column='PREGUNTA_37')  # Field name made lowercase.
    pregunta_38 = models.ForeignKey(CuestionarioTransevrsalPregunta38, models.DO_NOTHING, db_column='PREGUNTA_38')  # Field name made lowercase.
    pregunta_39 = models.ForeignKey(CuestionarioTransevrsalPregunta39, models.DO_NOTHING, db_column='PREGUNTA_39')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRANSVERSAL'


class CuestionarioTrayectoria(models.Model):
    id_cuestionario = models.AutoField(db_column='ID_CUESTIONARIO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='ID_USUARIO')  # Field name made lowercase.
    pregunta_1 = models.ForeignKey('CuestionarioTrayectoriaPregunta1', models.DO_NOTHING, db_column='PREGUNTA_1')  # Field name made lowercase.
    pregunta_2 = models.ForeignKey('CuestionarioTrayectoriaPregunta2', models.DO_NOTHING, db_column='PREGUNTA_2')  # Field name made lowercase.
    pregunta_3 = models.ForeignKey('CuestionarioTrayectoriaPregunta3', models.DO_NOTHING, db_column='PREGUNTA_3')  # Field name made lowercase.
    pregunta_4 = models.CharField(db_column='PREGUNTA_4', max_length=500)  # Field name made lowercase.
    pregunta_5 = models.ForeignKey('CuestionarioTrayectoriaPregunta5', models.DO_NOTHING, db_column='PREGUNTA_5')  # Field name made lowercase.
    pregunta_6 = models.ForeignKey('CuestionarioTrayectoriaPregunta6', models.DO_NOTHING, db_column='PREGUNTA_6')  # Field name made lowercase.
    pregunta_7 = models.ForeignKey('CuestionarioTrayectoriaPregunta7', models.DO_NOTHING, db_column='PREGUNTA_7')  # Field name made lowercase.
    pregunta_8 = models.PositiveIntegerField(db_column='PREGUNTA_8')  # Field name made lowercase.
    pregunta_9 = models.ForeignKey('CuestionarioTrayectoriaPregunta9', models.DO_NOTHING, db_column='PREGUNTA_9')  # Field name made lowercase.
    pregunta_10 = models.ForeignKey('CuestionarioTrayectoriaPregunta10', models.DO_NOTHING, db_column='PREGUNTA_10')  # Field name made lowercase.
    pregunta_11 = models.ForeignKey('CuestionarioTrayectoriaPregunta11', models.DO_NOTHING, db_column='PREGUNTA_11')  # Field name made lowercase.
    pregunta_12 = models.ForeignKey('CuestionarioTrayectoriaPregunta12', models.DO_NOTHING, db_column='PREGUNTA_12')  # Field name made lowercase.
    pregunta_13 = models.ForeignKey('CuestionarioTrayectoriaPregunta13', models.DO_NOTHING, db_column='PREGUNTA_13')  # Field name made lowercase.
    pregunta_14 = models.ForeignKey('CuestionarioTrayectoriaPregunta14', models.DO_NOTHING, db_column='PREGUNTA_14')  # Field name made lowercase.
    pregunta_15 = models.ForeignKey('CuestionarioTrayectoriaPregunta15', models.DO_NOTHING, db_column='PREGUNTA_15')  # Field name made lowercase.
    pregunta_16 = models.ForeignKey('CuestionarioTrayectoriaPregunta16', models.DO_NOTHING, db_column='PREGUNTA_16')  # Field name made lowercase.
    pregunta_17 = models.ForeignKey('CuestionarioTrayectoriaPregunta17', models.DO_NOTHING, db_column='PREGUNTA_17')  # Field name made lowercase.
    pregunta_18 = models.ForeignKey('CuestionarioTrayectoriaPregunta18', models.DO_NOTHING, db_column='PREGUNTA_18')  # Field name made lowercase.
    pregunta_19 = models.ForeignKey('CuestionarioTrayectoriaPregunta19', models.DO_NOTHING, db_column='PREGUNTA_19')  # Field name made lowercase.
    pregunta_20 = models.ForeignKey('CuestionarioTrayectoriaPregunta20', models.DO_NOTHING, db_column='PREGUNTA_20')  # Field name made lowercase.
    pregunta_21 = models.ForeignKey('CuestionarioTrayectoriaPregunta21', models.DO_NOTHING, db_column='PREGUNTA_21')  # Field name made lowercase.
    pregunta_22 = models.ForeignKey('CuestionarioTrayectoriaPregunta22', models.DO_NOTHING, db_column='PREGUNTA_22')  # Field name made lowercase.
    pregunta_23 = models.ForeignKey('CuestionarioTrayectoriaPregunta23', models.DO_NOTHING, db_column='PREGUNTA_23')  # Field name made lowercase.
    pregunta_24 = models.ForeignKey('CuestionarioTrayectoriaPregunta24', models.DO_NOTHING, db_column='PREGUNTA_24')  # Field name made lowercase.
    pregunta_25 = models.ForeignKey('CuestionarioTrayectoriaPregunta25', models.DO_NOTHING, db_column='PREGUNTA_25')  # Field name made lowercase.
    pregunta_26 = models.ForeignKey('CuestionarioTrayectoriaPregunta26', models.DO_NOTHING, db_column='PREGUNTA_26')  # Field name made lowercase.
    pregunta_27 = models.ForeignKey('CuestionarioTrayectoriaPregunta27', models.DO_NOTHING, db_column='PREGUNTA_27')  # Field name made lowercase.
    pregunta_28 = models.ForeignKey('CuestionarioTrayectoriaPregunta28', models.DO_NOTHING, db_column='PREGUNTA_28')  # Field name made lowercase.
    pregunta_29 = models.ForeignKey('CuestionarioTrayectoriaPregunta29', models.DO_NOTHING, db_column='PREGUNTA_29')  # Field name made lowercase.
    pregunta_30 = models.ForeignKey('CuestionarioTrayectoriaPregunta30', models.DO_NOTHING, db_column='PREGUNTA_30')  # Field name made lowercase.
    pregunta_31 = models.ForeignKey('CuestionarioTrayectoriaPregunta31', models.DO_NOTHING, db_column='PREGUNTA_31')  # Field name made lowercase.
    pregunta_32 = models.ForeignKey('CuestionarioTrayectoriaPregunta32', models.DO_NOTHING, db_column='PREGUNTA_32')  # Field name made lowercase.
    pregunta_33 = models.ForeignKey('CuestionarioTrayectoriaPregunta33', models.DO_NOTHING, db_column='PREGUNTA_33')  # Field name made lowercase.
    pregunta_34 = models.ForeignKey('CuestionarioTrayectoriaPregunta34', models.DO_NOTHING, db_column='PREGUNTA_34')  # Field name made lowercase.
    pregunta_35 = models.ForeignKey('CuestionarioTrayectoriaPregunta35', models.DO_NOTHING, db_column='PREGUNTA_35')  # Field name made lowercase.
    pregunta_36 = models.ForeignKey('CuestionarioTrayectoriaPregunta36', models.DO_NOTHING, db_column='PREGUNTA_36')  # Field name made lowercase.
    pregunta_37 = models.ForeignKey('CuestionarioTrayectoriaPregunta37', models.DO_NOTHING, db_column='PREGUNTA_37')  # Field name made lowercase.
    pregunta_38 = models.ForeignKey('CuestionarioTrayectoriaPregunta58', models.DO_NOTHING, db_column='PREGUNTA_38')  # Field name made lowercase.
    pregunta_39 = models.ForeignKey('CuestionarioTrayectoriaPregunta39', models.DO_NOTHING, db_column='PREGUNTA_39')  # Field name made lowercase.
    pregunta_40 = models.PositiveIntegerField(db_column='PREGUNTA_40')  # Field name made lowercase.
    pregunta_41 = models.PositiveIntegerField(db_column='PREGUNTA_41')  # Field name made lowercase.
    pregunta_42 = models.PositiveIntegerField(db_column='PREGUNTA_42')  # Field name made lowercase.
    pregunta_43 = models.PositiveIntegerField(db_column='PREGUNTA_43')  # Field name made lowercase.
    pregunta_44 = models.PositiveIntegerField(db_column='PREGUNTA_44')  # Field name made lowercase.
    pregunta_45 = models.PositiveIntegerField(db_column='PREGUNTA_45')  # Field name made lowercase.
    pregunta_46 = models.PositiveIntegerField(db_column='PREGUNTA_46')  # Field name made lowercase.
    pregunta_47 = models.PositiveIntegerField(db_column='PREGUNTA_47')  # Field name made lowercase.
    pregunta_48 = models.PositiveIntegerField(db_column='PREGUNTA_48')  # Field name made lowercase.
    pregunta_49 = models.PositiveIntegerField(db_column='PREGUNTA_49')  # Field name made lowercase.
    pregunta_50 = models.PositiveIntegerField(db_column='PREGUNTA_50')  # Field name made lowercase.
    pregunta_51 = models.PositiveIntegerField(db_column='PREGUNTA_51')  # Field name made lowercase.
    pregunta_52 = models.PositiveIntegerField(db_column='PREGUNTA_52')  # Field name made lowercase.
    pregunta_53 = models.PositiveIntegerField(db_column='PREGUNTA_53')  # Field name made lowercase.
    pregunta_54 = models.PositiveIntegerField(db_column='PREGUNTA_54')  # Field name made lowercase.
    pregunta_55 = models.PositiveIntegerField(db_column='PREGUNTA_55')  # Field name made lowercase.
    pregunta_56 = models.PositiveIntegerField(db_column='PREGUNTA_56')  # Field name made lowercase.
    pregunta_57 = models.PositiveIntegerField(db_column='PREGUNTA_57')  # Field name made lowercase.
    pregunta_58 = models.PositiveIntegerField(db_column='PREGUNTA_58')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA'


class CuestionarioTrayectoriaPregunta1(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_1'


class CuestionarioTrayectoriaPregunta10(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_10'


class CuestionarioTrayectoriaPregunta11(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_11'


class CuestionarioTrayectoriaPregunta12(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_12'


class CuestionarioTrayectoriaPregunta13(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_13'


class CuestionarioTrayectoriaPregunta14(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_14'


class CuestionarioTrayectoriaPregunta15(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_15'


class CuestionarioTrayectoriaPregunta16(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_16'


class CuestionarioTrayectoriaPregunta17(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_17'


class CuestionarioTrayectoriaPregunta18(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_18'


class CuestionarioTrayectoriaPregunta19(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_19'


class CuestionarioTrayectoriaPregunta2(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_2'


class CuestionarioTrayectoriaPregunta20(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_20'


class CuestionarioTrayectoriaPregunta21(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_21'


class CuestionarioTrayectoriaPregunta22(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_22'


class CuestionarioTrayectoriaPregunta23(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_23'


class CuestionarioTrayectoriaPregunta24(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_24'


class CuestionarioTrayectoriaPregunta25(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_25'


class CuestionarioTrayectoriaPregunta26(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_26'


class CuestionarioTrayectoriaPregunta27(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_27'


class CuestionarioTrayectoriaPregunta28(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_28'


class CuestionarioTrayectoriaPregunta29(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_29'


class CuestionarioTrayectoriaPregunta3(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_3'


class CuestionarioTrayectoriaPregunta30(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_30'


class CuestionarioTrayectoriaPregunta31(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_31'


class CuestionarioTrayectoriaPregunta32(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_32'


class CuestionarioTrayectoriaPregunta33(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_33'


class CuestionarioTrayectoriaPregunta34(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_34'


class CuestionarioTrayectoriaPregunta35(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_35'


class CuestionarioTrayectoriaPregunta36(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_36'


class CuestionarioTrayectoriaPregunta37(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_37'


class CuestionarioTrayectoriaPregunta38(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_38'


class CuestionarioTrayectoriaPregunta39(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_39'


class CuestionarioTrayectoriaPregunta40(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_40'


class CuestionarioTrayectoriaPregunta41(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_41'


class CuestionarioTrayectoriaPregunta42(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_42'


class CuestionarioTrayectoriaPregunta43(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_43'


class CuestionarioTrayectoriaPregunta44(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_44'


class CuestionarioTrayectoriaPregunta45(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_45'


class CuestionarioTrayectoriaPregunta46(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_46'


class CuestionarioTrayectoriaPregunta47(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_47'


class CuestionarioTrayectoriaPregunta48(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_48'


class CuestionarioTrayectoriaPregunta49(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_49'


class CuestionarioTrayectoriaPregunta5(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_5'


class CuestionarioTrayectoriaPregunta50(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_50'


class CuestionarioTrayectoriaPregunta51(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_51'


class CuestionarioTrayectoriaPregunta52(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_52'


class CuestionarioTrayectoriaPregunta53(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_53'


class CuestionarioTrayectoriaPregunta54(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_54'


class CuestionarioTrayectoriaPregunta55(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_55'


class CuestionarioTrayectoriaPregunta56(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_56'


class CuestionarioTrayectoriaPregunta57(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_57'


class CuestionarioTrayectoriaPregunta58(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_58'


class CuestionarioTrayectoriaPregunta6(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_6'


class CuestionarioTrayectoriaPregunta7(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_7'


class CuestionarioTrayectoriaPregunta8(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_8'


class CuestionarioTrayectoriaPregunta9(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUESTIONARIO_TRAYECTORIA_PREGUNTA_9'


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

    class Meta:
        managed = False
        db_table = 'UNIDAD_ACADEMICA'


class Usuario(models.Model):
    id_usuario = models.AutoField(db_column='ID_USUARIO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50)  # Field name made lowercase.
    apellido1 = models.CharField(db_column='APELLIDO1', max_length=50)  # Field name made lowercase.
    apellido2 = models.CharField(db_column='APELLIDO2', max_length=50)  # Field name made lowercase.
    curp = models.CharField(db_column='CURP', max_length=50)  # Field name made lowercase.
    sexo = models.CharField(db_column='SEXO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    edad = models.PositiveIntegerField(db_column='EDAD')  # Field name made lowercase.
    estado_civil = models.CharField(db_column='ESTADO_CIVIL', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=50)  # Field name made lowercase.
    pais = models.CharField(db_column='PAIS', max_length=200)  # Field name made lowercase.
    codigo_postal = models.CharField(db_column='CODIGO_POSTAL', max_length=10)  # Field name made lowercase.
    entidad_federativa = models.CharField(db_column='ENTIDAD_FEDERATIVA', max_length=200)  # Field name made lowercase.
    alcaldia_municipio = models.CharField(db_column='ALCALDIA_MUNICIPIO', max_length=200)  # Field name made lowercase.
    id_ua = models.ForeignKey(UnidadAcademica, models.DO_NOTHING, db_column='ID_UA')  # Field name made lowercase.
    id_pa = models.ForeignKey(ProgramaAcademico, models.DO_NOTHING, db_column='ID_PA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIO'
