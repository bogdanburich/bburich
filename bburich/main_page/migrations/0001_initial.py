# Generated by Django 2.2 on 2022-08-08 05:17

from django.db import migrations, models
import django.db.models.deletion
import main_page.validators


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
                ('logo', models.ImageField(upload_to='companies/', validators=[main_page.validators.validate_logo])),
                ('description', models.TextField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.URLField()),
                ('github', models.URLField()),
                ('link', models.URLField(blank=True, null=True)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('value', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Technologies',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=48)),
                ('start_at', models.DateField()),
                ('end_at', models.DateField()),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('employment_type', models.CharField(choices=[('FT', 'Full-time'), ('PT', 'Part-time')], default='FT', max_length=2)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='main_page.Company', verbose_name='Company')),
                ('skills', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experience', to='main_page.Skill', verbose_name='Skills')),
            ],
            options={
                'verbose_name_plural': 'Experience',
                'ordering': ['-start_at', '-employment_type'],
            },
        ),
    ]
