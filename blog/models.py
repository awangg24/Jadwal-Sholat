from django.db import models

# Create your models here.

class Tanggal(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Tanggal"

class Jadwal(models.Model):
    tanggal = models.CharField(max_length=100, blank=True, null=True)
    imsyak = models.CharField(max_length=100, blank=True, null=True)
    shubuh = models.CharField(max_length=100, blank=True, null=True)
    terbit = models.CharField(max_length=100, blank=True, null=True)
    dhuha = models.CharField(max_length=100, blank=True, null=True)
    dzuhur= models.CharField(max_length=100, blank=True, null=True)
    ashr = models.CharField(max_length=100, blank=True, null=True)
    magrib = models.CharField(max_length=100, blank=True, null=True)
    isya = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.tanggal, self.imsyak)

    class Meta:
        #ordering =['-tanggal']
        verbose_name_plural = "Jadwal"



class Sholat(models.Model):
    nama = models.CharField(max_length=30)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Sholat"

class Imam(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    hari = models.CharField(max_length=100)
    jam = models.CharField(max_length=100)
    sholata = models.ForeignKey(Sholat, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.nama, self.hari)

    class Meta:
        ordering =['-date']
        verbose_name_plural = "Imam"


class Nomor(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Nomor"

class Surah(models.Model):
    nomor = models.CharField(max_length=100, blank=True, null=True)
    nama = models.CharField(max_length=100, blank=True, null=True)
    nama_latin = models.CharField(max_length=100, blank=True, null=True)
    jumlah_ayat = models.CharField(max_length=100, blank=True, null=True)
    tempat_turun = models.CharField(max_length=100, blank=True, null=True)
    arti = models.CharField(max_length=100, blank=True, null=True)
    deskripsi = models.CharField(max_length=100, blank=True, null=True)
    audio = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.nomor, self.nama)

    class Meta:
        #ordering =['-nomor']
        verbose_name_plural = "Surah"