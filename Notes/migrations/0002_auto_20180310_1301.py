# Generated by Django 2.0.2 on 2018-03-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='Date',
            field=models.DateField(),
        ),
    ]
