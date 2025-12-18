from django.db import models
from registro.models import BaseModel


class Quarto(BaseModel):
    numero_quarto = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name='Número do Quarto',
        help_text='Insira o número do quarto'
    )
    tipo_quarto = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Tipo do Quarto',
        help_text='Insira o tipo do quarto (e.g., solteiro, casal, suíte)'
    )
    preco_diaria = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='Preço da Diária',
        help_text='Insira o preço da diária do quarto'
    )

    def __str__(self):
        return f"Quarto {self.numero_quarto} - {self.tipo_quarto}"