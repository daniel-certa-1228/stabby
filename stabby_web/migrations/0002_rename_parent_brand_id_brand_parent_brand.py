# Generated by Django 4.2.11 on 2024-04-12 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stabby_web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='parent_brand_id',
            new_name='parent_brand',
        ),
    ]