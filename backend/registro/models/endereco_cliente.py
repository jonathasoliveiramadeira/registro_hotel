from django.db import models
from registro.models import BaseModel


class EnderecoCliente(BaseModel):
    rua = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Rua',
        help_text='Insira o nome da rua'
    )
    numero = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name='Número',
        help_text='Insira o número do endereço'
    )
    bairro = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Bairro',
        help_text='Insira o bairro'
    )
    cidade = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Cidade',
        help_text='Insira a cidade'
    )
    estado = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Estado',
        help_text='Insira o estado'
    )
    cep = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name='CEP',
        help_text='Insira o CEP'
    )

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro} - {self.cidade}/{self.estado} - {self.cep}"