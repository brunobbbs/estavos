from django.db import models
from django.shortcuts import resolve_url as r
from mezzanine.pages.models import Page


class ClubPrice(models.Model):
    title = models.CharField('Identificador', help_text='Ex.: Mensal', max_length=50)
    value = models.DecimalField(
        'Valor mensalidade',
        max_digits=7,
        decimal_places=2,
        default='190.00'
    )
    active = models.BooleanField('Ativo?')
    notes = models.TextField('Observações', blank=True)
    club = models.ForeignKey('clubs.Club', related_name='prices')

    def __str__(self):
        return self.title


class ClubClass(models.Model):
    club = models.ForeignKey('clubs.Club', related_name='classes')
    klass = models.CharField('Turma', max_length=140)
    date = models.DateField('Data')
    hour = models.TimeField('Hora')

    class Meta:
        verbose_name = 'turma'
        verbose_name_plural = 'turmas'

    def __str__(self):
        return '{0}: {1} - {2}'.format(self.klass, self.date.strftime('%d/%m/%Y'), self.hour)


class Club(Page):
    name = models.CharField('Nome do clube', max_length=150)
    short_description = models.CharField('Descrição curta', max_length=350, blank=True)
    city = models.CharField('Cidade', max_length=100)
    district = models.CharField('Bairro', max_length=100)
    address = models.CharField('Endereço', max_length=100)
    phone = models.CharField('Telefone', max_length=200, blank=True)
    cover = models.ImageField(
        upload_to='clubs/cover/',
        verbose_name='Capa da página',
        help_text='Use uma imagem no tamanho 1170x500',
        blank=True,
        null=True
    )
    google_maps = models.TextField(
        'Mapa do local',
        blank=True,
        help_text='Insira um iframe do Google maps. Tamanho recomendado: 330x300'
    )
    inscription_link = models.URLField('Link para página de inscrição', blank=True, null=True)
