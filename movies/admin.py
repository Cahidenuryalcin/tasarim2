from django.contrib import admin
from .models import Category, Movie , Kategori, Malzeme, TarifMalzeme, Tur
# Register your models here.


admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Kategori)
admin.site.register(Malzeme)
admin.site.register(TarifMalzeme)
admin.site.register(Tur)