from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles', views.articles, name='articles'),
    url(r'^testimonials', views.testimonials, name='testimonials'),
    url(r'^user', views.user, name='user'),
    url(r'^vendor', views.vendor, name='vendor'),
]
    