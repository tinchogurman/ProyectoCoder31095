# Generated by Django 4.1 on 2022-10-14 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_alter_curso_camada_alter_estudiante_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='camada',
            field=models.IntegerField(),
        ),
    ]
