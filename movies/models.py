from django.db import models
from django.contrib.auth.models import User

# Create your models here. (veritabanı tabloları)

class Category(models.Model):
    name = models.CharField(max_length=100)
    
class Movie(models.Model):
    film_adi = models.CharField(max_length=200)
    resim = models.CharField(max_length=100)
    vakit= models.CharField(max_length=100 , default= 0)
    kisilik= models.CharField(max_length=100 , default= 0)
    defter= models.CharField(max_length=200 , default= 0)
    anasayfa = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    kalori = models.CharField(max_length=100 , default=0)
    tarif = models.CharField(max_length=5000, default=0)
    tmalzeme = models.CharField(max_length=5000, default=0)


class Kategori(models.Model):
    name = models.CharField(max_length=100)
   
class Malzeme(models.Model):
    malzeme_adi = models.CharField(max_length=200)
    malzeme_resim = models.CharField(max_length=100)
    malzeme_adet = models.PositiveIntegerField(default=0)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True, default=None)  # Kullanıcı ilişkisi
