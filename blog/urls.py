from django.urls import path, include
from . views import *

urlpatterns = [
    #apps
    path('', dashboard, name='dashboard'),
    path('jadwal/', jadwal, name='tabel_jadwal'),
    path('imam/', imam, name='tabel_imam'),
    path('surah/', surah, name='tabel_surah'),
    path('jadwal/tambah',tambah_jadwal, name='tambah_jadwal'),
    path('imam/tambah',tambah_imam, name='tambah_imam'),
    path('jadwal/lihat/<str:id>',lihat_jadwal, name='lihat_jadwal'),
    path('imam/lihat/<str:id>',lihat_imam, name='lihat_imam'),
    path('jadwal/edit/<str:id>',edit_jadwal, name='edit_jadwal'),
    path('imam/edit/<str:id>',edit_imam, name='edit_imam'),
    path('jadwal/delete/<str:id>',delete_jadwal, name='delete_jadwal'),
    path('imam/delete/<str:id>',delete_imam, name='delete_imam'),
    path('surah/delete/<str:id>',delete_surah, name='delete_surah'),
    path('users/', users, name='tabel_users'),
    path('calender/', calender, name='calender'),
]