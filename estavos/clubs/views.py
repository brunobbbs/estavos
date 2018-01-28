from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Club


class ClubDetail(DetailView):
    model = Club


class ClubList(ListView):
    model = Club
