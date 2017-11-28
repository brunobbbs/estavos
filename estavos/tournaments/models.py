# -*- coding: utf-8 -*-
from django.db import models
from estavos.utils.slug import unique_slugify
from django.utils.encoding import python_2_unicode_compatible
from django.shortcuts import resolve_url as r


class Tournament(models.Model):
    title = models.CharField('Nome do evento', max_length=100)
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateTimeField('Início')
    end_date = models.DateTimeField('Previsão de término')
    inscriptions_date_limit = models.DateTimeField('Data limite para inscrições')
    active = models.BooleanField('Ativo?')
    place = models.CharField('Local', max_length=50)
    url = models.URLField('Link da página do evento', blank=True, null=True)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(
        'Valor da inscrição',
        max_digits=7,
        decimal_places=2,
        default='20.00'
    )
    chess_results = models.URLField('Link para o ChessResults', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return r('tournaments:detail', self.pk)

    def save(self, **kwargs):
        unique_slugify(self, self.title)
        super(Tournament, self).save(**kwargs)


class Payment(models.Model):
    STATUS = (
        ("1", "Aguardando pagamento"),
        ("2", "Em análise"),
        ("3", "Paga"),
        ("4", "Disponível"),
        ("5", "Em disputa"),
        ("6", "Devolvida"),
        ("7", "Cancelada"),
    )

    TYPE = (
        ('1', 'PagSeguro'),
        ('2', 'Depósito bancário/Transferência'),
        ('3', 'Isenção')
    )

    paid = models.BooleanField('Pago?', default=False)
    payment_type = models.CharField(
        'Forma de pagamento',
        max_length=1,
        choices=TYPE,
        default='1'
    )
    receipt = models.FileField(
        upload_to='payments/receipts/',
        verbose_name='Recibo',
        blank=True,
        null=True,
    )
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    transaction = models.CharField(max_length=150, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_status_display()


class Competitor(models.Model):
    name = models.CharField('Nome do atleta', max_length=100)
    birth = models.DateField('Data de nascimento')
    id_lbx = models.CharField('ID LBX', max_length=7, blank=True,)
    id_fide = models.CharField(
        'ID FIDE',
        max_length=10,
        blank=True,
        help_text='Opcional. Informe se tiver um ID FIDE.'
    )
    club = models.CharField(
        'Escola/Clube',
        blank=True,
        max_length=100
    )
    inscription = models.ForeignKey('tournaments.Inscription', related_name='competitors')

    def __str__(self):
        return self.name

    def category(self):
        if self.birth.year >= 2010:
            return 'sub-07'

        elif self.birth.year >= 2008 and self.birth.year <= 2009:
            return 'sub-09'

        elif self.birth.year >= 2005 and self.birth.year <= 2007:
            return 'sub-12'

        elif self.birth.year >= 2002 and self.birth.year <= 2004:
            return 'sub-15'

        elif self.birth.year >= 1999 and self.birth.year <= 2001:
            return 'sub-18'

        else:
            return 'absoluto'

    category.short_description = 'Categoria'


class Inscription(models.Model):
    tournament = models.ForeignKey('tournaments.Tournament', related_name='inscriptions')
    name = models.CharField('Nome do responsável', max_length=100)
    email = models.EmailField()
    phone = models.CharField('Telefone', max_length=15, blank=True)
    confirmed = models.BooleanField('Confirmado?', default=False)
    slug = models.SlugField('Cod. Inscrição', max_length=32, unique=True)
    payment = models.ForeignKey('tournaments.Payment', blank=True, null=True, related_name='inscription')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Data/Hora inscrição')

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            import uuid
            slug = uuid.uuid4().hex
            self.slug = unique_slugify(self, slug)
        super(Inscription, self).save(**kwargs)

    def amount(self):
        players = self.competitors.all().count()
        price = self.tournament.price
        return players * price
