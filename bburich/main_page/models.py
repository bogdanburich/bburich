from django.db import models

from .validators import validate_github, validate_logo


class Company(models.Model):
    name = models.CharField(max_length=24)
    logo = models.FileField(
        upload_to='public/',
        validators=[validate_logo]
    )
    description = models.TextField(
        blank=True,
        max_length=256
    ),
    link = models.URLField()

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=24)
    value = models.IntegerField()

    class Meta:
        ordering = ['-value']

    def __str__(self):
        return self.name


class Instrument(models.Model):
    name = models.CharField(max_length=24)
    value = models.IntegerField()

    class Meta:
        ordering = ['-value']

    def __str__(self):
        return self.name


class Experience(models.Model):
    EMPLOYMENT_TYPES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time')
    ]

    role = models.CharField(max_length=48)
    start_at = models.DateField()
    end_at = models.DateField(
        blank=True,
        null=True
    )
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
    employment_type = models.CharField(
        max_length=2,
        choices=EMPLOYMENT_TYPES,
        default='FT'
    )

    class Meta:
        ordering = ['employment_type', '-start_at']
        verbose_name_plural = 'Experience'

    def __str__(self):
        return f'{self.company} | {self.role}'


class Project(models.Model):
    title = models.CharField(max_length=24)
    github = models.URLField(
        validators=[validate_github]
    )
    link = models.URLField(
        null=True,
        blank=True
    )
    description = models.TextField()
    date_added = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
