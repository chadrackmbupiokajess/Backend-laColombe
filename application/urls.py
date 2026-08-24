from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ServiceViewSet,
    EquipeViewSet,
    EquipementViewSet,
    SpaceViewSet,
    UtilisateurViewSet,
    csrf_token_view,
    login_view,
    logout_view,
    me_view,
    notifications_view,
    mark_notification_read,
)

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'equipe', EquipeViewSet)
router.register(r'equipements', EquipementViewSet)
router.register(r'spaces', SpaceViewSet)
router.register(r'utilisateurs', UtilisateurViewSet)

urlpatterns = [
    path('api/auth/csrf/', csrf_token_view, name='csrf-token'),
    path('api/auth/login/', login_view, name='login'),
    path('api/auth/logout/', logout_view, name='logout'),
    path('api/auth/me/', me_view, name='me'),
    path('api/notifications/', notifications_view, name='notifications'),
    path('api/notifications/<int:notification_id>/read/', mark_notification_read, name='mark-notification-read'),
    path('api/', include(router.urls)),
]
