# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.shortcuts import resolve_url as r, redirect
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from estavos.courses.forms import InscriptionForm
from estavos.courses.models import Inscription, Course


class Home(TemplateView):
    template_name = 'courses/index.html'

    def get_context_data(self, **kwargs):
        kwargs = super(Home, self).get_context_data(**kwargs)
        courses = Course.objects.filter(is_active=True)
        kwargs['num_open_classes'] = courses.count()
        kwargs['object_list'] = courses

        next_course = courses.filter(start_date__gt=datetime.date.today()).order_by('start_date')
        if next_course:
            next_course = next_course[0]
        kwargs['next_course'] = next_course
        return kwargs


class InscriptionCreate(CreateView):
    form_class = InscriptionForm
    model = Inscription

    def get_success_url(self):
        return r('courses:inscription_detail', self.object.slug)

    def _get_course(self):
        course = getattr(self, 'course', None)
        if not course:
            self.course = Course.objects.get(pk=self.kwargs['course_id'])
        return self.course

    def dispatch(self, request, *args, **kwargs):
        # If course is inactive, redirect to courses list page
        course = self._get_course()
        if not course.is_active:
            return redirect('courses:list')

        return super(InscriptionCreate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs = super(InscriptionCreate, self).get_context_data(**kwargs)
        kwargs['course'] = self._get_course()
        return kwargs
    
    def get_form(self, form_class=None):
        form = super(InscriptionCreate, self).get_form(form_class)
        form.instance.course = self.course
        return form


class InscriptionDetail(DetailView):
    model = Inscription


class CoursesListView(ListView):
    model = Course
    queryset = Course.objects.filter(is_active=True)
