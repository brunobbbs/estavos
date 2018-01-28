from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Club

admin.site.register(Club, PageAdmin)
