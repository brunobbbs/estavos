from django.views.generic import TemplateView, FormView
from estavos.courses.forms import InscriptionForm


class Home(TemplateView):
    template_name = 'courses/index.html'


class Inscription(FormView):
    template_name = 'courses/inscription.html'
    form_class = InscriptionForm