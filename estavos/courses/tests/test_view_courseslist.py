# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.test import TestCase
from django.shortcuts import resolve_url as r
from estavos.courses.models import Course


class CoursesListGet(TestCase):
    def setUp(self):
        self.course_inactive = Course.objects.create(
            name='Curso APRENDA #2',
            place='Núcleo de Xadrez do Clube ASCADE',
            start_date=date(2016, 02, 20),
            classes='Crianças',
            is_active=False
        )
        self.course = Course.objects.create(
            name='Curso APRENDA #3',
            place='Kumon Águas Claras - Av. das Castanheiras',
            start_date=date(2016, 03, 12),
            classes='Crianças',
            is_active=True
        )
        self.resp = self.client.get(r('courses:list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'courses/course_list.html')

    def test_view_should_return_only_active_courses(self):
        """View must return only active courses"""
        self.assertEqual(1, len(self.resp.context['object_list']))