from rest_framework.viewsets import ModelViewSet
from registro.models.quarto import Quarto
from registro.services.serializers.quarto_serializer import QuartoSerializer


class QuartoViewSet(ModelViewSet):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer