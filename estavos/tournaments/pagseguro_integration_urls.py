# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from estavos.tournaments.views import PagsguroPaymentDone


urlpatterns = [
    url(r'^compra-concluida/$', PagsguroPaymentDone.as_view(), name='payment_done'),
]
