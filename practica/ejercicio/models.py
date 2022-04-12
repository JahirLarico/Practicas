from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    edad=models.IntegerField()
    email=models.EmailField()
    telefono=models.CharField(max_length=100)
    carrera=models.CharField(max_length=100)
    pub_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre