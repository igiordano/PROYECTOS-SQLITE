# Generated by Django 5.1 on 2024-08-27 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=30)),
                ('marca_producto', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=30)),
                ('email_usuario', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas_detalles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField()),
                ('fecha_venta', models.DateField()),
                ('forma_de_pago', models.CharField(max_length=25)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.productos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.usuarios')),
            ],
        ),
    ]
