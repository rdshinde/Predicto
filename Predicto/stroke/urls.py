from django.urls import path
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    url(r'^favicon\.ico$',RedirectView.as_view(url='static/fevicon.ico')),
    path('',views.index,name='index'),
    # path('/prediction',views.PredictionView,name='prediction'),
    path('/about',views.about,name='about'),
    path('/resources',views.resources,name='resources'),
    
]