# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from estavos.tournaments.models import Inscription, Tournament


class InscriptionInline(admin.TabularInline):
    model = Inscription


class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'birth', 'phone', 'id_cbx', 'id_fide', 'confirmed')
    search_fields = ('name', 'email', 'id_cbx', 'id_fide')
    list_filter = ('confirmed', 'tournament')


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'inscriptions_date_limit',
                    'place', 'active')
    list_filter = ('start_date', 'end_date', 'active')
    inlines = (InscriptionInline, )
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(Tournament, TournamentAdmin)