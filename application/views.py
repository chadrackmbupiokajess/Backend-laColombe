from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Service, Equipe, EquipeCategory, Equipement, Space, Utilisateur, Notification
from .serializers import ServiceSerializer, EquipeSerializer, EquipeCategorySerializer, EquipementSerializer, SpaceSerializer, UtilisateurSerializer, NotificationSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def csrf_token_view(request):
    return Response({'csrfToken': get_token(request)})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    return Response({
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email,
        'is_staff': request.user.is_staff,
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'detail': 'Nom d’utilisateur et mot de passe requis.'}, status=400)

    user = authenticate(request, username=username, password=password)
    if user is None:
        return Response({'detail': 'Identifiants invalides.'}, status=401)

    if not user.is_active:
        return Response({'detail': 'Compte inactif.'}, status=403)

    login(request, user)
    return Response({
        'detail': 'Connexion réussie.',
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_staff': user.is_staff,
        }
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'detail': 'Déconnexion réussie.'})


@api_view(['GET'])
@permission_classes([AllowAny])
def notifications_view(request):
    notifications = Notification.objects.order_by('-created_at')[:20]
    unread_count = Notification.objects.filter(is_read=False).count()
    return Response({
        'count': unread_count,
        'results': NotificationSerializer(notifications, many=True).data,
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def mark_notification_read(request, notification_id):
    notification = Notification.objects.filter(id=notification_id).first()
    if not notification:
        return Response({'detail': 'Notification introuvable.'}, status=404)
    notification.is_read = True
    notification.save(update_fields=['is_read'])
    return Response({'detail': 'Notification marquée comme lue.', 'id': notification.id})


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer


class EquipeCategoryViewSet(viewsets.ModelViewSet):
    queryset = EquipeCategory.objects.all()
    serializer_class = EquipeCategorySerializer


class EquipementViewSet(viewsets.ModelViewSet):
    queryset = Equipement.objects.all()
    serializer_class = EquipementSerializer


class SpaceViewSet(viewsets.ModelViewSet):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer


class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
