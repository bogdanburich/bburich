# Generated by Django 2.2 on 2022-08-08 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_auto_20220808_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]