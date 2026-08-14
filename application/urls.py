from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, EquipeViewSet, EquipementViewSet, SpaceViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'equipe', EquipeViewSet)
router.register(r'equipements', EquipementViewSet)
router.register(r'spaces', SpaceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
