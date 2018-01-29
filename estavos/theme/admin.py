from django.contrib import admin
from estavos.theme.models import Banner


class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')


admin.site.register(Banner, BannerAdmin)
