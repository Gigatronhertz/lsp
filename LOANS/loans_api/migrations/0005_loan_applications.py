# Generated by Django 4.0.6 on 2022-07-30 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans_api', '0004_remove_loan_offers_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan_Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('Id', models.UUIDField()),
                ('applicant_id', models.UUIDField()),
                ('loan_offer_id', models.UUIDField()),
                ('amount_intended', models.FloatField()),
                ('amount_received', models.FloatField()),
                ('status', models.CharField(max_length=200)),
                ('approved_at', models.DateTimeField()),
                ('declined_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('loan_offers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans_api.loan_offers')),
            ],
        ),
    ]