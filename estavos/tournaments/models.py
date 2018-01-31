# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models
from estavos.utils.slug import unique_slugify
from django.utils.encoding import python_2_unicode_compatible
from django.shortcuts import resolve_url as r


class Prize(models.Model):
    title = models.CharField('Nome do prêmio', max_length=100)
    description = models.TextField('Descrição', blank=True)
    icon = models.CharField('Font-awesome icon. Ex.: "fa-trophy"', max_length=15, blank=True)
    tournament = models.ForeignKey('tournaments.Tournament', related_name='prizes')

    def __str__(self):
        return self.title


class InscriptionPrice(models.Model):
    title = models.CharField('Identificador', help_text='Ex.: 1º Lote', max_length=50)
    full = models.DecimalField(
        'Valor da inteira',
        max_digits=7,
        decimal_places=2,
        default='30.00'
    )
    limit_date = models.DateTimeField('Válido para inscrições realizadas até')
    active = models.BooleanField('Ativo?')
    notes = models.TextField('Observações', blank=True)
    tournament = models.ForeignKey('tournaments.Tournament', related_name='available_prices')

    def __str__(self):
        return self.title

    def valid_value(self):
        now = timezone.now()
        if self.limit_date < now:
            return False
        return True

    class Meta:
        ordering = ['limit_date']


class TournamentSchedule(models.Model):
    tournament = models.ForeignKey('tournaments.Tournament')
    date = models.DateField('Data')
    hour = models.TimeField('Hora')
    activity = models.CharField('Atividade', max_length=140)

    class Meta:
        verbose_name = 'programação'
        verbose_name_plural = 'programações'

    def __str__(self):
        return '{0} - {1}: {2}'.format(self.date.strftime('%d/%m/%Y'), self.hour, self.activity)


class Tournament(models.Model):
    MODALITIES = (
        ('classic', 'Clássico'),
        ('rapid', 'Rápido'),
        ('blitz', 'Relâmpago'),
    )

    title = models.CharField('Nome do evento', max_length=100)
    short_description = models.CharField('Descrição curta', max_length=250, blank=True)
    description = models.TextField('Descrição', blank=True)
    modality = models.CharField(
        'Modalidade',
        max_length=7,
        choices=MODALITIES,
        default='rapid'
    )
    cover = models.ImageField(
        upload_to='tournaments/cover/',
        verbose_name='Capa da página',
        help_text='Use uma imagem no tamanho 1170x500',
        blank=True,
        null=True
    )
    objective = models.TextField('Objetivos', blank=True)
    start_date = models.DateTimeField('Início')
    end_date = models.DateTimeField('Previsão de término')
    inscriptions_date_limit = models.DateTimeField('Data limite para inscrições')
    active = models.BooleanField('Ativo?')
    place = models.CharField('Local', max_length=50)
    google_maps = models.TextField(
        'Mapa do local do evento',
        blank=True,
        help_text='Insira um iframe do Google maps. Tamanho recomendado: 330x300'
    )
    rule = models.URLField('Link para download do regulamento')
    slug = models.SlugField(unique=True)
    price = models.DecimalField(
        'Valor da inscrição',
        max_digits=7,
        decimal_places=2,
        default='25.00'
    )
    chess_results = models.URLField('Link para o ChessResults', blank=True)
    pairing = models.CharField(
        'Sistema de disputa',
        max_length=30,
        help_text='Ex.: Suíço em 6 rodadas.',
        blank=True
    )
    game_time = models.CharField(
        'Tempo de reflexão',
        max_length=150,
        help_text="Ex.: 60'K.O",
        blank=True
    )
    notes = models.TextField('Observações gerais', blank=True)
    flyer = models.ImageField(
        'Folder do evento',
        upload_to='tournaments/flyers/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return r('tournaments:detail', self.slug)

    def save(self, **kwargs):
        unique_slugify(self, self.title)
        super(Tournament, self).save(**kwargs)

    def accept_inscriptions(self):
        now = timezone.now()
        if self.inscriptions_date_limit < now:
            return False
        return True


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
