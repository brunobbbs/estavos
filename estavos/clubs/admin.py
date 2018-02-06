from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Club


class ClubAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets)


admin.site.register(Club, ClubAdmin)
