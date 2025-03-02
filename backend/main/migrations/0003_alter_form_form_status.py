# Generated by Django 5.1.5 on 2025-03-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_otpverification_alter_user_email_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='form_status',
            field=models.CharField(choices=[('ready to calc', 'Ready To Calc'), ('draft', 'Draft'), ('pending', 'Pending'), ('verified', 'Verified')], default='draft', max_length=20),
        ),
    ]
