from django.views.generic import TemplateView
from mezzanine.pages.models import RichTextPage


class GaleriaView(TemplateView):
    template_name = 'pages/galeria.html'

    def get_context_data(self, **kwargs):
        kwargs = super(GaleriaView, self).get_context_data(**kwargs)
        evento = RichTextPage.objects.get(slug='galeria')
        kwargs['page'] = evento
        kwargs['galleries'] = self.galleries(evento)
        return kwargs

    def galleries(self, obj):
        galleries = obj.children.all()
        result = []

        for gallery in galleries:
            result.append({
                'title': gallery.title,
                'description': gallery.description,
                'url': gallery.get_absolute_url(),
                'img': gallery.gallery.images.order_by('?').first(),
                'keyword': gallery.keywords_string
            })
        return result