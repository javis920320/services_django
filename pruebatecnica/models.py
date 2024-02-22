from django.db import models

class Cliente(models.Model):
    ClienteID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Email = models.EmailField()
    Telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.Nombre
    


class Vehiculo(models.Model):
    VehiculoID = models.AutoField(primary_key=True)
    Marca = models.CharField(max_length=100)
    Modelo = models.CharField(max_length=100)
    Anio = models.IntegerField()
    Precio = models.DecimalField(max_digits=10, decimal_places=2)


class Concesionario(models.Model):
    ConcesionarioId = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=200)
    Ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre

class Transaccion(models.Model):
    TransaccionId = models.AutoField(primary_key=True)
    VehiculoId = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    ClienteId = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ConcesionarioId = models.ForeignKey(Concesionario, on_delete=models.CASCADE)
    FechaVenta = models.DateField()
    PrecioVenta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Transacción {self.TransaccionId}"   
  



    

