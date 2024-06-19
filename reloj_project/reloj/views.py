from django.shortcuts import render
from django.utils import timezone
from .models import Reloj

def mostrar_reloj(request):
    hora_actual = timezone.now().time()
    return render(request, 'reloj.html', {'hora_actual': hora_actual})
