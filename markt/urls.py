"""markt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from satici import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path("urun_ekle/",views.urun_ekle,name="urun_ekle"),
    path("urun_sil/<int:satici_id>",views.urun_sil,name="urun_sil"),
    path("urunler/<int:satici_id>",views.urunler,name="urunler"),
    path('satici/',include('satici.urls')),
    path('user/',include('user.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
