from rest_framework.viewsets import ModelViewSet
from registro.models.cliente import Cliente
from registro.services.serializers.cliente_serializer import ClienteSerializer
from rest_framework.permissions import IsAuthenticated


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cliente.objects.filter(usuario=self.request.user)
