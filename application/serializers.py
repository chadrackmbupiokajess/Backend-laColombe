from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Service, Equipe, Equipement, Space, Utilisateur


class AbsoluteImageMixin:
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image = getattr(instance, 'image', None)
        if image:
            request = self.context.get('request')
            data['image'] = request.build_absolute_uri(image.url) if request else image.url
        else:
            data['image'] = None
        return data


class ServiceSerializer(AbsoluteImageMixin, serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Service
        fields = ['id', 'name', 'text', 'image', 'order']


class EquipeSerializer(AbsoluteImageMixin, serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Equipe
        fields = ['id', 'name', 'role', 'text', 'image', 'order']


class EquipementSerializer(AbsoluteImageMixin, serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Equipement
        fields = ['id', 'name', 'text', 'image', 'order']


class SpaceSerializer(AbsoluteImageMixin, serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Space
        fields = ['id', 'name', 'text', 'image', 'order']


class UtilisateurSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Utilisateur
        fields = ['id', 'username', 'email', 'role', 'password', 'is_active']

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            validated_data['password'] = make_password(password)
        return super().update(instance, validated_data)
