from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home
# http://127.0.0.1:8000/movies
# http://127.0.0.1:8000/movies/3
# http://127.0.0.1:8000/movies/walking-dead

urlpatterns= [            
    path("", views.home2, name="home2"),
    path("home2", views.home2),
    path("home2", views.home2, name="home2"),
    path("yemektarifleri", views.yemektarifleri, name="yemektarifleri"),
    path("movies", views.movies , name="movies"),
    path("movies/<int:id>", views.moviedetails , name="moviedetails"), #detay sayfası için. doldurulacak
    path("kategori/<int:id>", views.moviesbycategory , name="moviesbycategory"), # kategoriye göre tarif filreleme
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('logmal/', views.malzeme_view, name='logmal'),
    path('kategoris/<int:id>/', views.malzemebycategory, name='malzemebycategory'),
    path('malzeme-ekle/', views.malzeme_ekle, name='malzeme_ekle'),
    path('yaptim/', views.yaptim, name='yaptim'),
    path('yukle/', views.yukle, name='yukle'),
    path("kullanicimal", views.kullanici_malzeme , name="kullanicimal"),
    path("malzeme/sil/<int:id>", views.malzeme_sil,name="malSil"),
    path("malzeme_duzenle/<int:id>", views.malzeme_duzenle,name="malzeme_duzenle"),
    path("benyaptim/<int:id>",views.benYaptim,name='benYaptim')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)