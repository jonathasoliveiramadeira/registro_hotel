from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ...permissions import IsOwner
from registro.models.reserva import Reserva
from registro.services.serializers.reserva_serializer import ReservaSerializer


class ReservaViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def get_queryset(self):
        return Reserva.objects.filter(usuario=self.request.user)
