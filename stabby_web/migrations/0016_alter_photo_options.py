# Generated by Django 5.0.6 on 2024-05-20 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stabby_web', '0015_alter_photo_options_alter_photo_knife_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['create_date'], 'verbose_name': 'photo', 'verbose_name_plural': 'photos'},
        ),
    ]
