from django.contrib import admin
from estavos.courses.models import Inscription, Course


class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'student')
    search_fields = ('name', 'student', 'email', 'phone')
    list_filter = ('created_at', )
    date_hierarchy = 'created_at'


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'start_date', 'classes', 'is_active')
    list_filter = ('start_date', )
    date_hierarchy = 'start_date'


admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(Course, CourseAdmin)
