# Generated by Django 4.2.8 on 2023-12-26 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0005_rename_asig_asignacion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='asignacion',
        ),
    ]
