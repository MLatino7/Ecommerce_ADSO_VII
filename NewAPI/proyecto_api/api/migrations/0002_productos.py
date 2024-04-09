# Generated by Django 5.0.2 on 2024-03-20 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=50)),
                ('id_categoria', models.PositiveIntegerField()),
                ('valor_unitario', models.PositiveIntegerField()),
                ('descripcionproducto', models.CharField(max_length=100)),
                ('fecha_modificacion', models.CharField(max_length=100)),
                ('estado_producto', models.CharField(max_length=100)),
            ],
        ),
    ]