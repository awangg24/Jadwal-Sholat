from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.db import transaction
from django.contrib.auth.hashers import make_password
import requests

from django.http import HttpResponse
from blog.models import Imam, Jadwal, Surah
from users.models import Biodata


def index(request):
    template_name = 'front/index.html'
    context = {
        'title':'jadwal sholatku',
    }
    return render(request, template_name, context)


def about(request):
    template_name = 'front/about.html'
    context = {
        'title':'about',
    }
    return render(request, template_name, context)


def isi_jadwal(request):
    url = "https://raw.githubusercontent.com/lakuapik/jadwalsholatorg/master/adzan/tenggarong/2022/12.json"
    data = requests.get(url).json()
    for d in data:
        cek_jadwal = Jadwal.objects.filter(tanggal=d['tanggal'])
        if cek_jadwal:
            print('data ada')
            e = cek_jadwal.first()
            e.tanggal=d['tanggal']
            e.save()
        else:
        #jika blm ada maka tulis ke db
            a =Jadwal.objects.create(
                tanggal = d['tanggal'],
                imsyak = d['imsyak'],
                shubuh = d['shubuh'],
                terbit = d['terbit'],
                dhuha = d['dhuha'],
                dzuhur = d['dzuhur'],
                ashr = d['ashr'],
                magrib = d['magrib'],
                isya = d['isya'],
            )
            
    template_name = 'front/isi_jadwal.html'
    jadwal = Jadwal.objects.all()
    context = {
        'title':'jadwal',
        'jadwal':jadwal,

    }
    return render(request, template_name, context)


def isi_imam(request):
    template_name = 'front/isi_imam.html'
    imam = Imam.objects.all()
    context = {
        'title':'imam',
        'imam':imam,
    }
    return render(request, template_name, context)


def login(request):
    template_name = "account/login.html"
    if request.user.is_authenticated:
        print('sudah login')
        return redirect('index')
        
    template_name = "account/login.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #ada data
            print('username benar')
            auth_login(request, user)
            return redirect('index')
        else:
            #tidak ada data
            print('username salah')
    context = {
        'title':'form login'
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('index')


def registrasi(request):
    template_name = "account/register.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email= request.POST.get('email')
        alamat= request.POST.get('alamat')
        nomer= request.POST.get('nomer')
        try:
            with transaction.atomic():
                User.objects.create(
                    username = username,
                    password = make_password(password),
                    first_name = first_name,
                    last_name = last_name,
                    email = email
                )
                get_user = User.objects.get(username = username)
                Biodata.objects.create(
                    user = get_user,
                    alamat = alamat,
                    telp = nomer,
                )
            return redirect(index)
        except:pass

    context = {
        'title':'form register'
    }
    return render(request, template_name, context)


def isi_surah(request):
    url = "https://equran.id/api/surat"
    data = requests.get(url).json()
    for s in data:
        cek_surah = Surah.objects.filter(nomor=s['nomor'])
        if cek_surah:
            print('data ada')
            a = cek_surah.first()
            a.nomor=s['nomor']
            a.save()
        else:
        #jika blm ada maka tulis ke db
            b =Surah.objects.create(
                nomor = s['nomor'],
                nama = s['nama'],
                nama_latin = s['nama_latin'],
                jumlah_ayat = s['jumlah_ayat'],
                tempat_turun = s['tempat_turun'],
                arti = s['arti'],
                deskripsi = s['deskripsi'],
                audio = s['audio'],
            )
            
    template_name = 'front/isi_surah.html'
    surah = Surah.objects.all()
    context = {
        'title':'surat',
        'surah':surah,

    }
    return render(request, template_name, context)

