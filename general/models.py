from django.db import models
from django.contrib.auth.models import User



class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)

    def __str__(self) -> str:
        return self.nombre



class comentarios(models.Model):
   
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()
    ranking = models.ForeignKey('Review', on_delete=models.CASCADE) 
    visible = models.BooleanField(default=True)


class Review(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f'{self.nombre}'

    
class Producto(models.Model):
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='producto/', blank=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    visible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.nombre}'

