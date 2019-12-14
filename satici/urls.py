from django.urls import path
from . import views

app_name='satici'

urlpatterns = [
    path("",views.index,name="index"),
    path("urunler/<int:satici_id>",views.urunler,name="urunler"),
    path("urun_ekle/",views.urun_ekle,name="urun_ekle"),
    path("urun_sil/<int:satici_id>",views.urun_sil,name="urun_sil"),
    path("urun_guncelle/<int:satici_id>",views.urun_guncelle,name="urun_guncelle"),
    path("about/",views.about,name="about"),
]