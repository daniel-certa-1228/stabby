# Generated by Django 4.2.11 on 2024-05-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stabby_web', '0005_viewbladegrid_viewknifegrid_viewsharpenergrid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blade',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='blade',
            name='length_cutting_edge',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='knife',
            name='closed_length',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='sharpener',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='sharpener',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True),
        ),
    ]
