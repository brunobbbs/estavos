# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from django.test import TestCase
from mezzanine.galleries.models import Gallery
from mezzanine.pages.models import  RichTextPage
from mezzanine.generic.models import AssignedKeyword, Keyword


class EventosGet(TestCase):
    def setUp(self):
        data = dict(title='Eventos', content='Eventos da Academia ESTAVOS')
        self.evento = RichTextPage.objects.create(**data)
        self._create_keywords()

        gallery_data = dict(title='Torneios', content='Torneios da ESTAVOS', parent=self.evento)
        t, _ = Keyword.objects.get_or_create(title="torneios")
        self.child = Gallery.objects.create(**gallery_data)
        self.child.keywords.add(AssignedKeyword(keyword=t))

        self.resp = self.client.get('/eventos/')

    def _create_keywords(self):
        s, _ = Keyword.objects.get_or_create(title="simultaneas")
        t, _ = Keyword.objects.get_or_create(title="torneios")
        c, _ = Keyword.objects.get_or_create(title="cursos")
        self.evento.keywords.add(AssignedKeyword(keyword=s))
        self.evento.keywords.add(AssignedKeyword(keyword=t))
        self.evento.keywords.add(AssignedKeyword(keyword=c))

    def test_get(self):
        """GET /eventos/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'pages/eventos.html')

    def test_keywords(self):
        KEYWORDS = (
            u'simultaneas',
            u'torneios',
            u'cursos'
        )
        for keyword in self.evento.keywords.all():
            self.assertIn(keyword.keyword.title, KEYWORDS)

    def test_context(self):
        """evento page should exists in context"""
        self.assertIsInstance(self.resp.context['page'], RichTextPage)
        self.assertIsInstance(self.resp.context['galleries'], list)

    def test_children(self):
        self.assertEqual(1, self.evento.children.count())

    def test_children_galleries(self):
        self.assertEqual(1, len(self.resp.context['galleries']))

    def test_children_gallery_keys(self):
        keys_expected = (
            'title', 'description', 'url', 'img', 'keyword'
        )
        for key in keys_expected:
            self.assertIn(key, self.resp.context['galleries'][0].keys())

    def test_children_gallery_values(self):
        gallery = self.resp.context['galleries'][0]
        self.assertEqual('Torneios', gallery['title'])
        self.assertEqual('Torneios da ESTAVOS', gallery['description'])
        self.assertEqual('/eventos/torneios/', gallery['url'])
        self.assertIn('torneios', gallery['keyword'])