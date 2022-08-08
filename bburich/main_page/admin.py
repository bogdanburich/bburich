from django.contrib import admin
from .models import Company, Experience, Skill, Instrument, Project


admin.site.site_header = 'Bogdan Burich website'
admin.site.register(Company)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Instrument)
admin.site.register(Project)
