# Generated by Django 4.1.4 on 2023-05-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cuestionario',
            fields=[
                ('id_cuestionario', models.AutoField(db_column='ID_CUESTIONARIO', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=200)),
                ('descripcion', models.CharField(db_column='DESCRIPCION', max_length=500)),
            ],
            options={
                'db_table': 'CUESTIONARIO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NivelAcademico',
            fields=[
                ('id_na', models.AutoField(db_column='ID_NA', primary_key=True, serialize=False)),
                ('nivel', models.CharField(blank=True, db_column='NIVEL', max_length=200, null=True)),
            ],
            options={
                'db_table': 'NIVEL_ACADEMICO',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadores',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta1',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta10',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta11',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta12',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta13',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta14',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta15',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta16',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta17',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta18',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta19',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta2',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta20',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta21',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta22',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta23',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta24',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta25',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta26',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta27',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta28',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta29',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta3',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta30',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta31',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta32',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta33',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta34',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta35',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta36',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta37',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta48',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta49',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta50',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta51',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta52',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta53',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta54',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta55',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta56',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta57',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta58',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta59',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta62',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta63',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta64',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta7',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta8',
        ),
        migrations.DeleteModel(
            name='CuestionarioEmpleadoresPregunta9',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta1',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta10',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta11',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta12',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta15',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta16',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta17',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta18',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta19',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta2',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta20',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta21',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta22',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta23',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta24',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta25',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta26',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta27',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta28',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta29',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta3',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta30',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta31',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta32',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta33',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta34',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta35',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta36',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta37',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta38',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta39',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta4',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta5',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta6',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta7',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta8',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransevrsalPregunta9',
        ),
        migrations.DeleteModel(
            name='CuestionarioTransversal',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoria',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta1',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta10',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta11',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta12',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta13',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta14',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta15',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta16',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta17',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta18',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta19',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta2',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta20',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta21',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta22',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta23',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta24',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta25',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta26',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta27',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta28',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta29',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta3',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta30',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta31',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta32',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta33',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta34',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta35',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta36',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta37',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta38',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta39',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta40',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta41',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta42',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta43',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta44',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta45',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta46',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta47',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta48',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta49',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta5',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta50',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta51',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta52',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta53',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta54',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta55',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta56',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta57',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta58',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta6',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta7',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta8',
        ),
        migrations.DeleteModel(
            name='CuestionarioTrayectoriaPregunta9',
        ),
    ]