from django.urls import path
from reloj.views import mostrar_reloj

urlpatterns = [
    path('reloj/', mostrar_reloj, name='reloj'),
]
