# Generated by Django 4.1.1 on 2022-09-06 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_rename_fechadeentrega_entregable_fecha_de_entrega_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='camada',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]