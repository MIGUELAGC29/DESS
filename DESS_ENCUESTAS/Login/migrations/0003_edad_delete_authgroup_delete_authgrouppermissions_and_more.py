# Generated by Django 4.1.4 on 2023-05-27 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edad',
            fields=[
                ('id_edad', models.AutoField(db_column='ID_EDAD', primary_key=True, serialize=False)),
                ('rango', models.CharField(db_column='RANGO', max_length=200)),
            ],
            options={
                'db_table': 'EDAD',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
    ]