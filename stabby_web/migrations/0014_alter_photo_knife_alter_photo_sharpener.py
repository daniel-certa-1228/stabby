# Generated by Django 5.0.6 on 2024-05-20 00:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stabby_web', '0013_remove_photo_name_photo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='knife',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photos', to='stabby_web.knife'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='sharpener',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photos', to='stabby_web.sharpener'),
        ),
    ]
