from django.conf.urls import url
from estavos.courses.views import CourseHome, CourseInscription

urlpatterns = [
    url(r'^$', CourseHome.as_view(), name='home'),
    url(r'^inscricao/$', CourseInscription.as_view(), name='inscription'),
]
