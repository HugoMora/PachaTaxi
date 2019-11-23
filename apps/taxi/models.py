from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    fecha_creacion = models.DateField('Fecha Creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    user     = models.OneToOneField(User, on_delete=models.CASCADE)
    rol      = models.ManyToManyField(Rol)
    alias    = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.User.first_name

class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=200, blank=False, null=False)        
    marca = models.CharField(max_length=200, blank=False, null=False)        
    color = models.CharField(max_length=200, blank=False, null=False)        
    imagen= models.ImageField(upload_to='pictures', max_length=255, null=True, blank=True)
    Id_usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    fecha_creacion = models.DateField('Fecha Creación', auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
        ordering = ['modelo']

    def __str__(self):
        return self.modelo

class Viaje(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    duracion = models.IntegerField()
    Tarifa = models.DecimalField(max_digits=5,decimal_places=2)
    estado= models.IntegerField()
    id_viajero= models.ForeignKey(User,on_delete=models.CASCADE, related_name='viajero')     
    id_conductor=models.ForeignKey(User, blank=True, null=True,on_delete=models.SET_NULL, related_name='conductor')
    fecha_creacion = models.DateField('Fecha Creación', auto_now=True, auto_now_add=False)
    es_favorito=models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Viaje'
        verbose_name_plural = 'Viajes'
        ordering = ['fecha']

    def __str__(self):
        return str(self.estado)




