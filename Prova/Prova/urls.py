from django.contrib import admin
from django.urls import path
from Site import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('depositar/', views.depositar, name='depositar'),
    path('sacar/', views.sacar, name='sacar'),
    path('iniciar-jogo/', views.iniciar_jogo, name='iniciar_jogo'),
]
