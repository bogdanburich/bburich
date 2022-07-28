from django.db import models
from .validators import validate_logo


class Company(models.Model):
    EMPLOYMENT_TYPES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time')
    ]

    name = models.CharField(max_length=24)
    logo = models.ImageField(
        upload_to='companies/',
        validators=[validate_logo]
    )
    description = models.TextField(
        blank=True,
        max_length=256
    )
    employment_type = models.CharField(
        max_length=2,
        choices=EMPLOYMENT_TYPES,
        default='FT'
    )

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=24)
    value = models.IntegerField()


class Technology(models.Model):
    name = models.CharField(max_length=24)
    value = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Technologies'


class Experience(models.Model):
    role = models.CharField(max_length=48)
    start_at = models.DateField()
    end_at = models.DateField()
    description = models.TextField(
        verbose_name='Description',
        blank=True
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='experience',
        verbose_name='Company'
    )
    skills = models.ForeignKey(
        Skill,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='experience',
        verbose_name='Skills'
    )
    technologies = models.ForeignKey(
        Technology,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='experience',
        verbose_name='Technologies'
    )

    class Meta:
        ordering = ['-start_at']
        verbose_name_plural = 'Experience'

    def __str__(self):
        return f'{self.company} | {self.role}'
