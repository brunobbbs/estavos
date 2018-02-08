from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Club, ClubClass, ClubClassTime, ClubPrice


class ClubPriceInline(admin.StackedInline):
    model = ClubPrice
    extra = 0
    min_num = 1


class ClubClassTimeInline(admin.StackedInline):
    model = ClubClassTime
    extra = 0
    min_num = 1


class ClubClassInline(admin.StackedInline):
    model = ClubClass
    extra = 0
    min_num = 1


class ClubClassAdmin(admin.ModelAdmin):
    list_display = ('club', 'name', 'weekday')
    list_filter = ('club',)
    inlines = (ClubClassTimeInline,)


class ClubAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets)
    inlines = (ClubClassInline, ClubPriceInline)


admin.site.register(ClubClass, ClubClassAdmin)
admin.site.register(Club, ClubAdmin)
