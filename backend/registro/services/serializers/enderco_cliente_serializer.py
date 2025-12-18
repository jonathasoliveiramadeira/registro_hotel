from rest_framework import serializers
from registro.models.endereco_cliente import EnderecoCliente


class EnderecoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoCliente
        fields = '__all__'