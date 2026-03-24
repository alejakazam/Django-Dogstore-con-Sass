from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('tienda/', views.tienda, name='tienda'),
    path('categoria/<slug:slug>/', views.productos_por_categoria, name='productos_categoria')   
]