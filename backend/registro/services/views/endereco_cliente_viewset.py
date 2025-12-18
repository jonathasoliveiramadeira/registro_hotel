from rest_framework.viewsets import ModelViewSet
from registro.models.endereco_cliente import EnderecoCliente
from registro.services.serializers.enderco_cliente_serializer import EnderecoClienteSerializer


class EnderecoClienteViewSet(ModelViewSet):
    queryset = EnderecoCliente.objects.all()
    serializer_class = EnderecoClienteSerializer