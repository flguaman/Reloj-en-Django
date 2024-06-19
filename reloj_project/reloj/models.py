from django.db import models
import datetime

class Reloj(models.Model):
    hora_actual = models.TimeField(default=datetime.time)

