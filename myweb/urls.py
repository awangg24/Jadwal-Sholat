from django.contrib import admin
from django.urls import path, include


############################ untuk media ############################
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500

from . views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('blog.urls')),
    #apps
    path('', index, name='index'),
    path('about', about, name='about'),
    path('jadwal/isi_jadwal/', isi_jadwal, name='isi_jadwal'),
    path('jadwal/isi_imam/', isi_imam, name='isi_imam'),
    path('surah/isi_surah/', isi_surah, name='isi_surah'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registrasi, name='registrasi'),
]


############################ untuk media ############################
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
