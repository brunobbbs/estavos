from django.contrib import admin
from estavos.courses.models import Inscription


class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'student')
    search_fields = ('name', 'student', 'email', 'phone')
    list_filter = ('created_at', )
    date_hierarchy = 'created_at'


admin.site.register(Inscription, InscriptionAdmin)
