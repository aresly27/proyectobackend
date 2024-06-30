from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Usuario
from .serializers import UsuarioSerializer, CambiarPasswordSerializer
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model


# Create your views here.

User = get_user_model()
class CreateUsuario(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        data = request.data
        email = data.get('email')
        print("Request Data:", data)
        
        if Usuario.objects.filter(email=email).exists():
            return Response({"error": "Ya existe un usuario con este email."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UsuarioSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            print("Token Created:", token.key)
            response = {
                'success':True,
                'user':serializer.data,
                'token':token.key
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditUsuario(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, usuario_id):
        usuario_obj = get_object_or_404(Usuario, id=usuario_id)
        serializer = UsuarioSerializer(instance=usuario_obj, data=request.data, partial=True )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def delete(self, request, usuario_id):
        usuario_obj = get_object_or_404(Usuario, pk=usuario_id)
        usuario_obj.is_active=False
        usuario_obj.save()
        return Response({'message':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        data = request.data
        
        user = get_object_or_404(Usuario, email=data['email'])
        
        if not user.check_password(data['password']):
            return Response({'error':'Contraseña incorrecta'}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        serializer = UsuarioSerializer(instance=user)

        return Response({'token':token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
    
class LoginAuth(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        data = request.data
        response = {"mensaje":"Usuario autenticado",
                    }
        return Response(response)
    

class CambiarPassword(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = CambiarPasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # Actualizar la contraseña
            serializer.update(request.user, serializer.validated_data)
            return Response({"detail": "Contraseña actualizada exitosamente."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)