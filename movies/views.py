from audioop import reverse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Category, Fotograf, Movie, Kategori, Malzeme, KullaniciMalzeme,TarifMalzeme,KullaniciTarif
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

import cv2
import numpy as np
import os


# Create your views here.

# kategori_liste =["macera", "romatik","dram", "bilim kurgu"]
# film_liste=[
#     { 
#       "id" : 1,
#       "film_adi" : "film 1",
#       "aciklama" : "film 1 aciklama",
#       "resim" : "1.jpeg",
#       "anasayfa" : True
#     },
#     { 
#       "id" : 2,
#       "film_adi" : "film 2",
#       "aciklama" : "film 2 aciklama",
#       "resim" : "2.jpeg",
#       "anasayfa" : True
#     },
#     {
#       "id" : 3,
#       "film_adi" : "film 3",
#       "aciklama" : "film 3 aciklama",
#       "resim" : "3.jpeg",
#       "anasayfa" : False
#     },
#     {
#       "id" : 4,
#       "film_adi" : "film 4",
#       "aciklama" : "film 4 aciklama",
#       "resim" : "4.jpeg",
#       "anasayfa" : False
#     }
# ]

def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.filter(anasayfa=True)
    }
    return render(request, "index.html",data)

def home2(request):
    return render(request, "index2.html")

def yemektarifleri(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all(),
     
    }
    return render(request, "menu2.html", data)

def movies(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all(),
     
    }
    return render(request, "menu2.html", data)

def moviedetails(request,id):

    control = False

    if request.user.is_authenticated:
        control = KullaniciTarif.objects.filter(user=request.user, tarif_id=id).exists()



    data = {
        "movie": Movie.objects.get(id=id),
        "malzemeler": TarifMalzeme.objects.filter(movie=id),
        "control": control
    }
    return render(request, "moviedetails.html",data)

def moviesbycategory(request, id):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.filter(category__id=id),
        "selected": id
     
    }
    return render(request, "menu2.html",data)


def login_request(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("logmal")
        else:
            return render(request, "login.html" , {
                "error": "kullanıcı adı ya da parola yanlış"
            })
      
    return render(request, "login.html")


def register_request(request):
    if request.method == "POST":
        username= request.POST["username"]
        firstname= request.POST["firstname"]
        lastname= request.POST["lastname"]
        email= request.POST["email"]
        password= request.POST["password"]
        password_confirm= request.POST["password_confirm"]

        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                 return render(request, "register.html", 
                 {
                 "error": "kullanıcı adı bulunuyor.",
                 "username":username,
                 "firstname":firstname,
                 "lastname":lastname,
                 "email":email

                 })
            else:
                if User.objects.filter(email=email).exists():
                 return render(request, "register.html", 
                 {
                 "error": "email kullanılıyor.",
                 "username":username,
                 "firstname":firstname,
                 "lastname":lastname,
                 "email":email
                 
                 })
                else:
                    user = User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password)
                    user.save()
                    return redirect("login")
        else:
            return render(request, "register.html", 
            {
            "error": "parola eşleşmiyor.",
            "username":username,
            "firstname":firstname,
            "lastname":lastname,
            "email":email
                 
            })
        
    return render(request, "register.html")

def logout_request(request):
    logout(request)
    return redirect("home2")

@login_required(login_url='login')
def kullanici_malzeme(request):
    data = {
            "malzemeler": KullaniciMalzeme.objects.filter(user_id=request.user.id)
            
        }
    return render(request, "kullanicimal.html",data)

def malzeme_view(request):
   
    data = {
        "malzemekategori": Kategori.objects.all(),
        "malzemeler": KullaniciMalzeme.objects.filter(user_id=request.user.id),  
    }
    return render(request, "logmal.html", data)

@login_required
def malzemebycategory(request, id):
    kategori = get_object_or_404(Kategori, id=id)
    malzemeler = KullaniciMalzeme.objects.filter(malzeme__kategori=kategori,user_id=request.user.id)

    data = {
        "malzemekategori": Kategori.objects.all(),
        "malzemeler": malzemeler,
        "selecteds": id
    }
    return render(request, "logmal.html", data)

@login_required
def malzeme_ekle(request):
    if request.method == 'POST':
        malzeme_id = request.POST.get('malzeme_id')
        adet = request.POST.get('adet')

        malzeme = KullaniciMalzeme(malzeme_id=malzeme_id,adet=adet,user_id= request.user.id)
        malzeme.save()

        return redirect('logmal')  # Yönlendirme yapılacak sayfa
    

    existing_malzemeler = KullaniciMalzeme.objects.filter(user_id=request.user.id).values_list('malzeme_id', flat=True)
    malzemeler = Malzeme.objects.exclude(id__in=existing_malzemeler)



    data = {
        "malzemeler": malzemeler,
    }
    return render(request, "malzeme_ekle.html", data)

@login_required
def malzeme_sil(request,id):

    malzemeler = KullaniciMalzeme.objects.filter(user_id=request.user.id,malzeme_id=id)
    malzemeler.delete()
       
    return redirect("logmal")

def yaptim(request):
    return render(request, 'yaptim.html')


@login_required
def malzeme_duzenle(request,id):
    malzeme = KullaniciMalzeme.objects.get(user_id=request.user.id,malzeme_id=id)

    if request.method=='POST':
        malzeme.adet = request.POST.get('adet')
        malzeme.save()
        
        return redirect("logmal")
    
    data={
        "malzeme": malzeme
    }

    return render(request,"malzeme_duzenle.html",data)


def yaptim(request):
    return render(request, 'yaptim.html')


def yukle(request):
   if request.method == 'POST':
        photo = request.FILES.get('photo')  # Dosya alındı

        # Veritabanına kaydetme
        new_photo = Fotograf(foto=photo)
        new_photo.save()

      

        return render(request, 'goruntule.html', {'photo': new_photo})

   return render(request, 'yaptim.html')

# İşlevin amacı, belirli bir yemeğin tarif malzemelerini kullanarak kullanıcının kaynaklarını güncellemektir.
@login_required(login_url='login') #  kullanıcının oturum açmış olamlı
def benYaptim(request, id):  # İşlevin adı benYaptim ve iki parametre alıyor: request ve id.
    tarif_malzemeler = TarifMalzeme.objects.filter(movie=id) #İşlevin içindeki ilk satır, TarifMalzeme modelinden, yemeğin id değeriyle eşleşen tarif malzemelerini alır.

    for tarif_malzeme in tarif_malzemeler:
        try:
            kullanici_malzeme = KullaniciMalzeme.objects.get(malzeme=tarif_malzeme.malzeme_id,user_id=request.user.id)
            kullanilan_adet = TarifMalzeme.objects.get(malzeme=tarif_malzeme.malzeme_id, movie=id)

            kullanici_malzeme.adet -= kullanilan_adet.kullanilan_adet
            if kullanici_malzeme.adet < 0:
                kullanici_malzeme.adet = 0
            kullanici_malzeme.save()

            KullaniciTarif.objects.create(tarif_id=id, user_id=request.user.id)

        except KullaniciMalzeme.DoesNotExist:
            pass

    return redirect('moviedetails', id=id)

