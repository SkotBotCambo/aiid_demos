from django.contrib import admin

# Register your models here.
from .models import Incident, Report
admin.site.register(Incident)
admin.site.register(Report)
