from django.db import models
from registro.models import BaseModel
from django.contrib.auth.models import User
from .quarto import Quarto
from .cliente import Cliente


class Reserva(BaseModel):
    cliente_nome = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_entrada = models.DateField(
        null=False,
        blank=False,
        verbose_name='Data de Entrada',
        help_text='Insira a data de entrada da reserva'
    )
    data_saida = models.DateField(
        null=False,
        blank=False,
        verbose_name='Data de Saída',
        help_text='Insira a data de saída da reserva'
    )
    quantidade_pessoas = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Quantidade de Pessoas',
        help_text='Insira a quantidade de pessoas para a reserva'
    )
    valor_reserva = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='Valor da Reserva',
        help_text='Insira o valor total da reserva'
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reservas'
    )
    quarto = models.ForeignKey(
        Quarto,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Reserva de {self.data_entrada} a {self.data_saida} para {self.cliente_nome}"