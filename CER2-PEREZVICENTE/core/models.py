from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class LugarPatrimonial(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    ubicacion = models.CharField(max_length=200)
    anio_construccion = models.IntegerField()
    imagen = models.URLField(help_text="Enlace de la imagen", blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    destacado = models.BooleanField(default=False)

    def __str__(self):
            return self.nombre
    