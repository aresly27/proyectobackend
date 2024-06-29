from rest_framework import serializers
from .models import Usuario
from django.contrib.auth import get_user_model

User = get_user_model()
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','username', 'email', 'password', 'nombre', 'fecha_nac', 'imagen']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            nombre=validated_data['nombre'],
            fecha_nac=validated_data['fecha_nac'],
            imagen=validated_data.get('imagen', '')
        )
        return user