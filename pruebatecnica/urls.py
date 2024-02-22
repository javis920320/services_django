from django.urls import path, include
from rest_framework import routers
from pruebatecnica import views

router = routers.DefaultRouter()
router.register(r'Cliente', views.ClientViewSet, 'Cliente')
router.register(r'Vehiculo', views.VehiculoViewSet, 'vehiculo')
router.register(r'Concesionario', views.ConcesionarioViewSet, 'concesionario') 
router.register(r'Transacion', views.TransacciónViewSet, 'transacción') 
 # Corregir esta línea



urlpatterns = [
    path("api/v1/", include(router.urls))
]
