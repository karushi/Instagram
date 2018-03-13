from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'index'),
    url('^profile/',views.profile, name= 'profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url('^comments/(?P<id>\d+)', views.comment, name='comment'),
    url(r'^upload_image/',views.upload,name='upload'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)