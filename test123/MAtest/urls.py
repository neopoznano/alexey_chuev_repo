from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import redirect_original, shorten_url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('mainpage/', views.mainpage, name="mainpage"),
    url(r'^(?P<short_id>\w{6})$', redirect_original, name='redirectoriginal'),
    url(r'^makeshort/$', shorten_url, name='shortenurl'),
]
