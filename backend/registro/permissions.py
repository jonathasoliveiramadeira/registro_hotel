from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """
    Permite edição apenas do dono do objeto.
    Leitura pode ser controlada separadamente.
    """

    def has_object_permission(self, request, view, obj):
        # Permite métodos seguros para qualquer usuário (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True

        # Permite edição apenas se o usuário for o dono do objeto (PUT, PATCH, DELETE)
        return obj.usuario == request.user
