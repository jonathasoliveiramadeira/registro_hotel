from rest_framework import serializers
from registro.models.quarto import Quarto


class QuartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarto
        fields = '__all__'