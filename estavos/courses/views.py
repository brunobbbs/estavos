from django.views.generic import TemplateView


class CourseHome(TemplateView):
    template_name = 'courses/index.html'


class CourseInscription(TemplateView):
    template_name = 'courses/inscription.html'