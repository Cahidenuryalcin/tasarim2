from audioop import reverse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from .models import Category, Movie, Kategori, Malzeme
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

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

def movies(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all(),
     
    }
    return render(request, "movies.html",data)

def moviedetails(request,id):
    data = {
        "movie": Movie.objects.get(id=id)
    }
    return render(request, "moviedetails.html",data)

def moviesbycategory(request, id):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.filter(category__id=id),
        "selected": id
     
    }
    return render(request, "movies.html",data)


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
                "error": "username ya da parola yanlış"
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
    return redirect("home")



def malzeme_view(request):
   
    if request.method == 'POST':
        malzeme_id = request.POST.get('malzeme_id')
        if malzeme_id:
            try:
                malzeme = get_object_or_404(Malzeme, id=malzeme_id)
                if 'increment' in request.POST:
                    malzeme.malzeme_adet += 1
                elif 'decrement' in request.POST:
                    malzeme.malzeme_adet -= 1
                malzeme.save()
            except Malzeme.DoesNotExist:
                pass
            
    malzemeler = Malzeme.objects.filter(user=request.user)  # Kullanıcının malzemelerini filtrele
    data = {
        "malzemekategori": Kategori.objects.all(),
        "malzemeler": Malzeme.objects.all(),
        
       
        
    }
    return render(request, "logmal.html", data)

@login_required
def malzemebycategory(request, id):
    kategori = get_object_or_404(Kategori, id=id)
    malzemeler = Malzeme.objects.filter(kategori=kategori)

    data = {
        "malzemekategori": Kategori.objects.all(),
        "malzemeler": malzemeler,
        "selecteds": id
    }
    return render(request, "logmal.html", data)

@login_required
def malzeme_ekle(request):
    if request.method == 'POST':
        malzeme_adi = request.POST.get('malzeme_adi')
        malzeme_adet = request.POST.get('malzeme_adet')
        kategori_id = request.POST.get('kategori')

        kategori = get_object_or_404(Kategori, id=kategori_id)

        malzeme = Malzeme(malzeme_adi=malzeme_adi, malzeme_adet=malzeme_adet, kategori=kategori)
        malzeme.save()

        return redirect('logmal')  # Yönlendirme yapılacak sayfa

    data = {
        "malzemekategori": Kategori.objects.all(),
    }
    return render(request, "malzeme_ekle.html", data)
