from django.urls import path
from . import views

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home
# http://127.0.0.1:8000/movies
# http://127.0.0.1:8000/movies/3
# http://127.0.0.1:8000/movies/walking-dead

urlpatterns= [            
    path("", views.home, name="home"),
    path("home", views.home),
    path("movies", views.movies , name="movies"),
    path("movies/<int:id>", views.moviedetails , name="moviedetails"), #detay sayfası için. doldurulacak
    path("kategori/<int:id>", views.moviesbycategory , name="moviesbycategory"), # kategoriye göre tarif filreleme
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/logmal/', views.malzeme_view, name='logmal'),
    path('kategoris/<int:id>/', views.malzemebycategory, name='malzemebycategory'),
    path('malzeme-ekle/', views.malzeme_ekle, name='malzeme_ekle')

]