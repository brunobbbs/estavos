# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from estavos.tournaments.models import Inscription, Tournament, Payment, Competitor
from import_export.admin import ImportExportModelAdmin


class InscriptionInline(admin.StackedInline):
    model = Inscription


class CompetitorInline(admin.StackedInline):
    model = Competitor


class PaymentAdmin(ImportExportModelAdmin):
    list_display = ('payment_type', 'status', 'paid', 'receipt')
    list_filter = ('paid', 'status', 'payment_type')
    inlines = [InscriptionInline]


class CompetitorAdmin(ImportExportModelAdmin):
    list_display = ('name', 'birth', 'id_lbx', 'id_fide')
    list_filter = ('id_lbx', 'id_fide')


class InscriptionAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email', 'phone', 'confirmed')
    search_fields = ('name', 'email')
    list_filter = ('confirmed', 'tournament')
    inlines = [CompetitorInline]


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'inscriptions_date_limit',
                    'place', 'active')
    list_filter = ('start_date', 'end_date', 'active')
    inlines = (InscriptionInline, )
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Competitor, CompetitorAdmin)
admin.site.register(Tournament, TournamentAdmin)
