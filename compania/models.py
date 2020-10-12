from django.db import models

# Create your models here.

class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.nombre_ciudad

#
class Titulo(models.Model):
    nombre_titulo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Titulo'
        verbose_name_plural = 'Titulos'

    def __str__(self):
        return self.nombre_titulo

class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=255)
    ciudad_empleado = models.ForeignKey(Ciudad, related_name='ciudad_empleado', on_delete=models.CASCADE, verbose_name='Ciudad')
    titulo_empleado = models.ForeignKey(Titulo, related_name='titulo_empleado', on_delete=models.CASCADE, verbose_name='Titulo')

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre_empleado

