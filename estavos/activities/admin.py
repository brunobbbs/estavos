from django.contrib import admin
from estavos.activities.models import Activity, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'description', 'transport', 'partner', 'duration')
    search_fields = ('description', )
    list_filter = ('date', 'partner', 'category')
    date_hierarchy = 'date'


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Category, CategoryAdmin)