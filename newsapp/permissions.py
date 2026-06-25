from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение: только автор может редактировать/удалять свою новость.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешено чтение для всех
        if request.method in permissions.SAFE_METHODS:
            return True

        # Редактирование/удаление только для автора
        return obj.author == request.user