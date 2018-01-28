from django.db import models
from django.shortcuts import resolve_url as r
from mezzanine.pages.models import Page


class Club(Page):
    name = models.CharField('Nome do clube', max_length=150)
