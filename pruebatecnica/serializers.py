from rest_framework import serializers
from .models import Cliente,Vehiculo,Concesionario,Transaccion


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['ClienteID', 'Nombre', 'Email', 'Telefono']
        #serializar todo fields="__all__"

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehiculo
        fields="__all__"


class ConcesionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Concesionario
        fields = ['ConcesionarioId', 'Nombre', 'Direccion', 'Ciudad']



class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaccion
        fields = ['TransaccionId', 'VehiculoId', 'ClienteId', 'ConcesionarioId', 'FechaVenta', 'PrecioVenta']