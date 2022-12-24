from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.models import User

from .models import *
# Create your views here.

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False



@login_required
def dashboard(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] ='operator'

    template_name = 'back/dashboard.html'
    context = {
        'title':'dashboard',

    }
    return render(request, template_name, context)


def jadwal(request):
    template_name = 'back/tabel_jadwal.html'
    jadwal = Jadwal.objects.all()
    #for j in jadwal:
    #   print(j.imsyak, '-', j.shubuh, '-',j.kotam)
    context = {
        'title':'tabel jadwal',
        'jadwal':jadwal,

    }
    return render(request, template_name, context)

def imam(request):
    template_name = 'back/backag/tabel_imam.html'
    imam = Imam.objects.all()
    #for i in imam:
    #   print(i.nama, '-', i.hari, '-',i.sholata)
    context = {
        'title':'tabel imam',
        'imam':imam,

    }
    return render(request, template_name, context)


def surah(request):
    template_name = 'back/backsh/tabel_surah.html'
    surah = Surah.objects.all()
    #for i in imam:
    #   print(i.nama, '-', i.hari, '-',i.sholata)
    context = {
        'title':'tabel surah',
        'surah':surah,

    }
    return render(request, template_name, context)


def tambah_jadwal(request):
    template_name = "back/tambah_jadwal.html"
    tanggal = Tanggal.objects.all()
    print(tanggal)
    if request.method == "POST":
        tanggal = request.POST.get('tanggal')
        imsyak = request.POST.get('imsyak')
        shubuh= request.POST.get('shubuh')
        terbit = request.POST.get('terbit')
        dhuha = request.POST.get('dhuha')
        dzuhur = request.POST.get('dzuhur')
        ashr = request.POST.get('ashr')
        magrib = request.POST.get('magrib')
        isya = request.POST.get('isya')

        #panggil kota dulu
        tag = Tanggal.objects.get(nama=tanggal)
        
        Jadwal.objects.create(
            tanggal= tanggal,
            imsyak = imsyak,
            shubuh = shubuh,
            terbit = terbit,
            dhuha = dhuha,
            dzuhur = dzuhur,
            ashr = ashr,
            magrib = magrib,
            isya = isya,
        )
        return redirect(jadwal)
    context = {
        'title': 'tambah jadwal',
        'tanggal':tanggal,
    }
    return render(request, template_name, context)


def tambah_imam(request):
    template_name = "back/backag/tambah_imam.html"
    sholata = Sholat.objects.all()
    print(sholata)
    if request.method == "POST":
        nama = request.POST.get('nama')
        hari = request.POST.get('hari')
        jam = request.POST.get('jam')
        sholata = request.POST.get('sholata')

        #panggil sholata dulu

        sho = Sholat.objects.get(nama=sholata)

        Imam.objects.create(
            nama = nama,
            hari = hari,
            jam = jam,
            sholata = sho,
        )
        return redirect(imam)
    context = {
        'title': 'tambah imam',
        'sholata':sholata,
    }
    return render(request, template_name, context)

    template_name = "back/backsh/tambah_surah.html"
    nomor = Nomor.objects.all()
    print(nomor)
    if request.method == "POST":
        nomor= request.POST.get('nomor')
        nama = request.POST.get('nama')
        nama_latin= request.POST.get('nama_latin')
        jumlah_ayat = request.POST.get('jumlah_ayat')
        tempat_turun = request.POST.get('tempat_turun')
        arti = request.POST.get('arti')
        deskripsi = request.POST.get('deskripsi')

        #panggil nomor dulu

        no = Nomor.objects.get(nama=nomor)

        Surah.objects.create(
            nomor = nomor,
            nama = nama,
            nama_latin = nama_latin,
            jumlah_ayat = jumlah_ayat,
            tempat_turun = tempat_turun,
            arti = arti,
            deskripsi = deskripsi,
            audio = audio,
        )
        return redirect(surah)
    context = {
        'title': 'tambah surah',
        'nomor':nomor,
    }
    return render(request, template_name, context)


def lihat_jadwal(request, id):
    template_name = "back/lihat_jadwal.html"
    jadwal = Jadwal.objects.get(id=id)
    context = {
        'title':'lihat jadwal',
        'jadwal':jadwal,
    }
    return render(request, template_name, context)

def lihat_imam(request, id):
    template_name = "back/backag/lihat_imam.html"
    imam = Imam.objects.get(id=id)
    context = {
        'title':'lihat imam',
        'imam':imam,
    }
    return render(request, template_name, context)


def edit_jadwal(request, id):
    template_name = "back/edit_jadwal.html"
    j = Jadwal.objects.get(id=id)
    if request.method == "POST":
        imsyak = request.POST.get("imsyak")
        shubuh= request.POST.get("shubuh")
        terbit = request.POST.get("terbit")
        dhuha = request.POST.get("dhuha")
        dzuhur = request.POST.get("dzuhur")
        ashr = request.POST.get("ashr")
        magrib = request.POST.get("magrib")
        isya = request.POST.get("isya")
        # simpan
        j.imsyak = imsyak
        j.shubuh = shubuh
        j.terbit = terbit
        j.dhuha = dhuha
        j.dzuhur = dzuhur
        j.ashr = ashr
        j.magrib= magrib
        j.isya = isya
        j.save()
        return redirect(jadwal)

    context = {
        'title':'edit jadwal',
        'jadwal':j,
    }
    return render(request, template_name, context)



def edit_imam(request, id):
    template_name = "back/backag/edit_imam.html"
    i = Imam.objects.get(id=id)
    if request.method == "POST":
        nama = request.POST.get('nama')
        hari = request.POST.get('hari')
        jam = request.POST.get('jam')
        sholata = request.POST.get('sholata')
        # simpan
        i.nama = nama
        i.hari = hari
        i.jam = jam
        i.save()
        return redirect(imam)

    context = {
        'title':'edit imam',
        'imam':i,
    }
    return render(request, template_name, context)



def delete_jadwal(request, id):
    Jadwal.objects.get(id=id).delete()
    return redirect(jadwal)


def delete_imam(request, id):
    Imam.objects.get(id=id).delete()
    return redirect(imam)

def delete_surah(request, id):
    Surah.objects.get(id=id).delete()
    return redirect(surah)


@user_passes_test(is_operator)
def users(request):
    template_name = 'back/tabel_users.html'
    user_list = User.objects.all
    context = {
        'title':'tabel users',
        'user_list':user_list,

    }
    return render(request, template_name, context)


def calender(request):
    template_name = 'back/calender.html'
    context = {
        'title':'calender',
    }
    return render(request, template_name, context)