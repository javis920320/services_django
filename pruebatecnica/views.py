
from rest_framework import viewsets
from .serializers import ClienteSerializer,VehiculoSerializer,ConcesionarioSerializer,TransaccionSerializer
from .models import Cliente,Vehiculo,Concesionario,Transaccion

# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class=ClienteSerializer
    queryset=Cliente.objects.all()

class VehiculoViewSet(viewsets.ModelViewSet):
    serializer_class=VehiculoSerializer
    queryset=Vehiculo.objects.all()

class ConcesionarioViewSet(viewsets.ModelViewSet):
     serializer_class=ConcesionarioSerializer
     queryset=Concesionario.objects.all()

class TransacciónViewSet(viewsets.ModelViewSet):
    serializer_class=TransaccionSerializer
    queryset=Transaccion.objects.all()
