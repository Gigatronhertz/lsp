# Generated by Django 4.0.6 on 2022-07-28 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_offers',
            name='minimum_duration',
            field=models.FloatField(),
        ),
    ]