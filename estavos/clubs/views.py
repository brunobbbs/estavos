from django.shortcuts import render
from django.views.generic import DetailView, ListView
from mezzanine.core.models import CONTENT_STATUS_PUBLISHED
from .models import Club


class ClubList(ListView):
    model = Club
    queryset = Club.objects.filter(status=CONTENT_STATUS_PUBLISHED)
