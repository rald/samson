from django.urls import path

from . import views

from jinki.views import Cpage;

urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('Fpage', views.Fpage, name='Fpage'),
    path('Cpage', Cpage.as_view()),
]
