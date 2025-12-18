from django.core.validators import MinLengthValidator
from django.db import models
from registro.models import BaseModel
from .endereco_cliente import EnderecoCliente
from django.conf import settings


class Cliente(BaseModel):
    nome = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(10)],
        verbose_name='Nome',
        help_text='Insira o nome do cliente',
        default=''
    )
    cpf = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(5)],
        verbose_name='CPF',
        help_text='Insira o cpf do cliente',
        default=''
    )
    telefone = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        verbose_name='Telefone',
        help_text='Insira o telefone do cliente'
    )
    endereco = models.ForeignKey(
        EnderecoCliente,
        on_delete=models.CASCADE,
        verbose_name='Endereço',
        help_text='Insira o endereço do cliente'
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='clientes',
        verbose_name='Usuário'
    )

    def __str__(self):
        return f"{self.nome}"
