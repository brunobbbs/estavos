from django.contrib import admin
from estavos.theme.models import Banner, Partner


class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')


admin.site.register(Banner, BannerAdmin)
admin.site.register(Partner, PartnerAdmin)
