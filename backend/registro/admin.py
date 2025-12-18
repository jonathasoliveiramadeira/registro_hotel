from django.contrib import admin
from registro.models import Cliente, EnderecoCliente, Quarto, Reserva

# Register your models here.
admin.site.register(Cliente)
admin.site.register(EnderecoCliente)
admin.site.register(Quarto)
admin.site.register(Reserva)