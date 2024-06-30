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
    
class CambiarPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("La contraseña actual es incorrecta.")
        return value
    
    def validate_new_password(self, value):
        # Aquí puedes agregar validaciones adicionales para la nueva contraseña si lo deseas
        return value
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
    