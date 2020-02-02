from django.contrib import admin
from .models import job
# Register your models here.

class jobAdmin(admin.ModelAdmin):
    list_display = ('image', 'summary')
    search_fields = ('summary',)
    list_filter = ('image', 'summary')

admin.site.register(job,jobAdmin)