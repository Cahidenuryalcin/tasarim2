from django.db import models
from django.contrib.auth.models import User


# Create your models here. (veritabanı tabloları)

class Kategori(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tur(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Malzeme(models.Model):
    malzeme_adi = models.CharField(max_length=200)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    tur = models.ForeignKey(Tur, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.malzeme_adi


class KullaniciMalzeme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    malzeme = models.ForeignKey(Malzeme, on_delete=models.CASCADE)
    adet = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)




class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    film_adi = models.CharField(max_length=200)
    resim = models.CharField(max_length=100)
    vakit= models.CharField(max_length=100 , default= 0)
    kisilik= models.CharField(max_length=100 , default= 0)
    defter= models.CharField(max_length=200 , default= 0)
    anasayfa = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    kalori = models.CharField(max_length=100 , default=0)
    tarif = models.CharField(max_length=5000, default=0) #tarif

    def __str__(self):
        return self.film_adi

class TarifMalzeme(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    malzeme = models.ForeignKey(Malzeme, on_delete=models.CASCADE)
    kullanilan_adet = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.movie.film_adi} - {self.malzeme.malzeme_adi} - {self.kullanilan_adet}"
    
class Fotograf(models.Model):
    foto = models.ImageField(upload_to='uploads')


class KullaniciTarif(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    tarif=models.ForeignKey(Movie,on_delete=models.CASCADE)