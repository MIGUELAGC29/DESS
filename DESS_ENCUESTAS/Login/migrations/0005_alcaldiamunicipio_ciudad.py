# Generated by Django 4.1.4 on 2023-05-30 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_pais'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlcaldiaMunicipio',
            fields=[
                ('id_alc_mun', models.AutoField(db_column='ID_ALC_MUN', primary_key=True, serialize=False)),
                ('alcaldia_municipio', models.CharField(blank=True, db_column='ALCALDIA_MUNICIPIO', max_length=200, null=True)),
            ],
            options={
                'db_table': 'ALCALDIA_MUNICIPIO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.AutoField(db_column='ID_CIUDAD', primary_key=True, serialize=False)),
                ('ciudad', models.CharField(blank=True, db_column='CIUDAD', max_length=200, null=True)),
            ],
            options={
                'db_table': 'CIUDAD',
                'managed': False,
            },
        ),
    ]
