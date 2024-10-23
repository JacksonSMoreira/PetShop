from django.contrib import admin
from reserva.models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display =['nome', 'email', 'nome_pet', 'data', 'turno']
    serch_fields = ['nome', 'email', 'nome_pet']
    list_display = ['data', 'turno', 'tamanho']
