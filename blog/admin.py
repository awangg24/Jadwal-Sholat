from django.contrib import admin
from .models import *

# Register your models here.

class JadwalAdmin(admin.ModelAdmin):
  list_display = ('tanggal','imsyak','shubuh','terbit','dhuha','dzuhur','ashr','magrib','isya')

admin.site.register(Tanggal)
admin.site.register(Jadwal, JadwalAdmin)


class ImamAdmin(admin.ModelAdmin):
  list_display = ('nama','hari','jam','sholata','date')

admin.site.register(Sholat)
admin.site.register(Imam, ImamAdmin)


class SurahAdmin(admin.ModelAdmin):
  list_display = ('nomor','nama','nama_latin','jumlah_ayat','tempat_turun','arti','deskripsi','audio')
admin.site.register(Nomor)
admin.site.register(Surah, SurahAdmin)


