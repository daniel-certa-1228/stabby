# Generated by Django 5.0.6 on 2024-09-30 22:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stabby_web', '0023_delete_viewsteeltypechart'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewKnifeBladeGrid',
            fields=[
                ('knife_id', models.BigIntegerField(db_column='knife_id', primary_key=True, serialize=False)),
                ('blade_shape_id', models.BigIntegerField()),
                ('knife', models.CharField(max_length=255, null=True)),
                ('knife_type', models.CharField(max_length=255, null=True)),
                ('brand', models.CharField(max_length=255, null=True)),
                ('num_of_blades', models.IntegerField(null=True)),
                ('blade_material', models.CharField(max_length=255, null=True)),
                ('handle_material', models.CharField(max_length=255, null=True)),
                ('lock_type', models.CharField(max_length=255, null=True)),
                ('deployment_type', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('vendor', models.CharField(max_length=255, null=True)),
                ('needs_work', models.BooleanField()),
                ('purchased_new', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('create_date', models.DateTimeField()),
                ('user_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'view_knife_blade_grid',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photos', to='stabby_web.brand'),
        ),
    ]
