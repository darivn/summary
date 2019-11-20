from django.contrib import admin
from .models import Background, Experience
# Register your models here.
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('institution_name', 'specialization', 'level', 'year_start')
    search_fields = ('institution_name', 'specialization', 'level', 'year_start')

admin.site.register(Background, BackgroundAdmin)
admin.site.register(Experience)