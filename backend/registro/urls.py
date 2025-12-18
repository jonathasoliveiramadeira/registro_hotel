from rest_framework.routers import DefaultRouter
from .services.views import ClienteViewSet, ReservaViewSet, QuartoViewSet, EnderecoClienteViewSet


router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'quartos', QuartoViewSet)
router.register(r'enderecos', EnderecoClienteViewSet)

urlpatterns = router.urls