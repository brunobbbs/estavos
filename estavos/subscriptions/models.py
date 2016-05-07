from django.db import models
from django.utils.translation import ugettext_lazy as _
from newsletter_subscription.models import SubscriptionBase


class Subscription(SubscriptionBase):
    first_name = models.CharField(_('Seu primeiro nome'), max_length=20, blank=True)
