# Generated by Django 2.2 on 2022-07-28 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('logo', models.ImageField(upload_to='companies/')),
                ('employment_type', models.CharField(choices=[('FT', 'Full-time'), ('PT', 'Part-time')], default='FT', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=48)),
                ('start_at', models.DateField()),
                ('end_at', models.DateField()),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='main_page.Company', verbose_name='Company')),
            ],
            options={
                'ordering': ['-start_at'],
            },
        ),
    ]
