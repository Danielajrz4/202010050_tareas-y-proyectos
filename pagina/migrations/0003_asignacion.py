# Generated by Django 4.2.8 on 2023-12-26 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_metodopago_nit_alter_metodopago_codigo_de_seguridad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pagina.product')),
            ],
        ),
    ]
