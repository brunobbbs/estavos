from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
from mezzanine.blog.models import BlogPost
from mezzanine.pages.models import RichTextPage

from estavos.theme.gapi_calendar import GApiCalendar


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


class HomeView(TemplateView):
    template_name = 'index.html'

    @method_decorator(cache_page(600))
    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['blog_post_list'] = BlogPost.objects.all()[:3]
        gapi = GApiCalendar()
        kwargs['upcoming_events'] = gapi.get_upcoming_events()
        return kwargs
