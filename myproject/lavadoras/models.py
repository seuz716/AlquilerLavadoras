# lavadoras/models.py
from django.contrib.auth.models import User  
from django.db import models

class Lavadora(models.Model):
    nombre = models.CharField(max_length=100)
    horas_de_vida_util = models.PositiveIntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    consumo_de_energia_kw_h = models.DecimalField(max_digits=5, decimal_places=2)
    horas_de_uso_acumulado = models.PositiveIntegerField(default=0)
    horas_de_uso_mantenimiento = models.PositiveIntegerField()
    proximo_mantenimiento = models.DateTimeField()
    
    def __str__(self):
        return self.nombre

class Alquiler(models.Model):
    lavadora = models.ForeignKey(Lavadora, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    horas_de_uso = models.PositiveIntegerField()
    fecha_alquiler = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.lavadora.nombre}"
