# Generated by Django 4.0.4 on 2022-09-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0002_rename_amout_transaction_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtn_api_account',
            name='api_key_disb',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='mtn_api_account',
            name='operator',
            field=models.CharField(choices=[('MTN', 'MTN'), ('ORANGE', 'ORANGE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='operator',
            field=models.CharField(choices=[('MTN', 'MTN'), ('ORANGE', 'ORANGE')], max_length=50),
        ),
    ]
