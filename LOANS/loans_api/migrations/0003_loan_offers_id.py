# Generated by Django 4.0.6 on 2022-07-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans_api', '0002_alter_loan_offers_minimum_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan_offers',
            name='Id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
