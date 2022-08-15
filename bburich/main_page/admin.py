from django.contrib import admin

from .forms import ExperienceAdminForm
from .models import Company, Experience, Instrument, Project, Skill


class ExperienceAdmin(admin.ModelAdmin):
    form = ExperienceAdminForm


admin.site.site_header = 'Bogdan Burich website'
admin.site.register(Company)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill)
admin.site.register(Instrument)
admin.site.register(Project)
