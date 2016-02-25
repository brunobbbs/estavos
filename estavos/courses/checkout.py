# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import get_object_or_404, resolve_url as r
from django.views.generic import RedirectView
from estavos.courses.models import Inscription
from pagseguro.api import PagSeguroItem, PagSeguroApi


class PagseguroCheckout(RedirectView):

    permanent = False

    def get_object(self, slug):
        obj = getattr(self, 'obj', None)
        if not obj:
            self.obj = get_object_or_404(Inscription, slug=slug)
        return self.obj

    def pagseguro(self, inscription):
        item = PagSeguroItem(
            id=inscription.course.pk,
            description=inscription.course.name,
            amount=inscription.course.price,
            quantity=1
        )

        pg = PagSeguroApi(
            reference=inscription.pk,
            senderEmail=inscription.email
        )

        pg.add_item(item)
        data = pg.checkout()

        if data.get('success'):
            return data['redirect_url']

        else:
            messages.error(
                self.request,
                'Houve um erro ao processar seus dados. Se o problema persistir entre em contato: '
                '(61) 8121-7870 ou (61) 9193-0933'
            )
            return r("courses:list")

    def get_redirect_url(self, *args, **kwargs):
        inscription = self.get_object(kwargs['slug'])
        url = self.pagseguro(inscription)
        return url
