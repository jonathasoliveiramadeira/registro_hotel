# ============================================================
# COMANDO CUSTOMIZADO DO DJANGO PARA GERAR LOCAÇÕES AUTOMÁTICAS
# ============================================================

# Biblioteca padrão do Python para trabalhar com valores aleatórios
# Usaremos para escolher usuários, quartos, dias de estadia etc.
import random

# Classe usada para somar/subtrair dias de uma data
# Muito útil para calcular data de saída a partir da entrada
from datetime import timedelta

# Classe base obrigatória para qualquer comando customizado do Django
# Sem isso o Django não reconhece o comando
from django.core.management.base import BaseCommand

# Model de usuário padrão do Django
# Usaremos para definir quem é o "dono" da locação
from django.contrib.auth.models import User

# Utilitário de datas do Django
# Garante compatibilidade com TIME_ZONE e USE_TZ
from django.utils import timezone

# Importação dos models do sistema
# Locacao = registro principal
# Quarto = relacionamento obrigatório
from registro.models import Reserva, Quarto


# ============================================================
# CLASSE PRINCIPAL DO COMANDO
# O nome *PRECISA* ser "Command"
# ============================================================
class Command(BaseCommand):

    # Texto de ajuda exibido ao rodar: python manage.py help
    help = 'Gera reservas automáticas para testes do sistema de hotel'

    # ========================================================
    # MÉTODO PRINCIPAL
    # É executado automaticamente quando rodamos o comando
    # ========================================================
    def handle(self, *args, **options):

        # ====================================================
        # 1️⃣ BUSCAR USUÁRIOS DO SISTEMA
        # ====================================================

        # Busca todos os usuários cadastrados no banco
        usuarios = User.objects.all()

        # Se não existir nenhum usuário, o script é interrompido
        # Evita erro e deixa claro o motivo
        if not usuarios.exists():
            self.stdout.write(
                self.style.ERROR(
                    'Nenhum usuário encontrado. Crie usuários antes de rodar o script.'
                )
            )
            return  # Encerra a execução do comando

        # ====================================================
        # 2️⃣ BUSCAR QUARTOS CADASTRADOS
        # ====================================================

        # Busca todos os quartos existentes no banco
        quartos = Quarto.objects.all()

        # Se não houver quartos, não é possível criar locações
        if not quartos.exists():
            self.stdout.write(
                self.style.ERROR(
                    'Nenhum quarto encontrado. Cadastre quartos antes de rodar o script.'
                )
            )
            return  # Encerra a execução do comando

        # ====================================================
        # 3️⃣ DEFINIR QUANTIDADE DE REGISTROS
        # ====================================================

        # Quantidade de locações que serão criadas
        # Você pode alterar esse valor livremente
        total_registros = 20

        # Mensagem informativa no terminal
        self.stdout.write(
            f'Iniciando criação de {total_registros} locações...'
        )

        # ====================================================
        # 4️⃣ LOOP PRINCIPAL DE CRIAÇÃO
        # ====================================================

        # Para cada iteração, uma nova locação será criada
        for i in range(total_registros):

            # ------------------------------------------------
            # DATA DE ENTRADA
            # ------------------------------------------------

            # Gera uma data de entrada entre hoje e até 30 dias atrás
            # Isso deixa os dados mais realistas
            data_entrada = timezone.now() - timedelta(
                days=random.randint(1, 30)
            )

            # ------------------------------------------------
            # TEMPO DE ESTADIA
            # ------------------------------------------------

            # Define aleatoriamente quantos dias o cliente ficará
            # Mínimo: 1 dia | Máximo: 7 dias
            dias_estadia = random.randint(1, 7)

            # Calcula a data de saída somando os dias de estadia
            data_saida = data_entrada + timedelta(days=dias_estadia)

            # ------------------------------------------------
            # USUÁRIO (DONO DA LOCAÇÃO)
            # ------------------------------------------------

            # Escolhe um usuário aleatório da lista
            # Esse usuário será o dono do registro
            usuario = random.choice(usuarios)

            # ------------------------------------------------
            # QUARTO DA LOCAÇÃO
            # ------------------------------------------------

            # Escolhe um quarto aleatório disponível no banco
            quarto = random.choice(quartos)

            # ------------------------------------------------
            # QUANTIDADE DE PESSOAS
            # ------------------------------------------------

            # Define aleatoriamente entre 1 e 4 pessoas no quarto
            quantidade_pessoas = random.randint(1, 4)

            # ------------------------------------------------
            # CRIAÇÃO DA LOCAÇÃO NO BANCO
            # ------------------------------------------------

            # Aqui o Django:
            # - valida os campos
            # - executa regras do model
            # - salva no banco
            # - dispara signals (se existirem)
            Reserva.objects.create(
                usuario=usuario,                 # Dono da locação
                quarto=quarto,                   # Quarto escolhido
                data_entrada=data_entrada,       # Data de entrada
                data_saida=data_saida,           # Data de saída
                quantidade_pessoas=quantidade_pessoas
            )

            # Mensagem simples para acompanhamento do progresso
            self.stdout.write(
                f'Reserva {i + 1} criada com sucesso.'
            )

        # ====================================================
        # 5️⃣ FINALIZAÇÃO DO SCRIPT
        # ====================================================

        # Mensagem final em verde indicando sucesso total
        self.stdout.write(
            self.style.SUCCESS(
                f'{total_registros} reservas criadas com sucesso!'
            )
        )
