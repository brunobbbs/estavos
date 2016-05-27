# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms


class InscriptionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    birth = forms.DateField()
    id_cbx = forms.CharField()
    id_fide = forms.CharField()
    phone = forms.CharField()
