from django.contrib import admin
from django.urls import path
from Site import views
from Site.views import salvar_nota

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('salvar-nota/', salvar_nota, name='salvar_nota'),
]
