from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Evaluacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(default=now)
    documento = models.CharField(max_length=20)
    tipo_evalua = models.CharField(max_length=20, choices=[
        ('Evaluación', 'Evaluación'),
        ('Coevaluación', 'Coevaluación'),
        ('Autoevaluación', 'Autoevaluación')
    ])
    responsabilidad = models.IntegerField()
    sentido_de_pertenencia = models.IntegerField()
    trabajo_en_equipo = models.IntegerField()
    liderazgo = models.IntegerField()
    humanizacion = models.IntegerField()
    seguridad = models.IntegerField()
    observaciones = models.TextField()
    promedio = models.FloatField()

    def save(self, *args, **kwargs):
        # Calcula el promedio automáticamente
        self.promedio = sum([
            self.responsabilidad,
            self.sentido_de_pertenencia,
            self.trabajo_en_equipo,
            self.liderazgo,
            self.humanizacion,
            self.seguridad
        ]) / 6
        super().save(*args, **kwargs)
