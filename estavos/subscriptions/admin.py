from django.contrib import admin
from estavos.subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'is_active')


admin.site.register(Subscription, SubscriptionAdmin)