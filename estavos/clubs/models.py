from django.db import models
from django.shortcuts import resolve_url as r
from mezzanine.pages.models import Page


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
