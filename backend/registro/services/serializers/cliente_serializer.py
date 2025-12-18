from rest_framework import serializers
from registro.models.cliente import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["nome"]