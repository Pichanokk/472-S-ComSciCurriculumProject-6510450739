# Generated by Django 5.1.5 on 2025-03-12 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_notpasscourse_subcategory_fk_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategorydetails',
            old_name='credit_details_fk',
            new_name='credit_detail_fk',
        ),
    ]
