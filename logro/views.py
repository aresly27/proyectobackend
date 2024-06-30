from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Logro
from .serializers import LogroSerializer
from django.http import JsonResponse
import random
import json


class LogroCreateView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        data = request.data
        serializer = LogroSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'message':'Creado'}, status=status.HTTP_201_CREATED)
    
class EditLogro(APIView):
    #permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)

    def put(self, request, logro_id):
        logro_obj = get_object_or_404(Logro, id=logro_id)
        serializer = LogroSerializer(instance=logro_obj, data=request.data, partial=True )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, logro_id):
        logro_obj = get_object_or_404(Logro, pk=logro_id)
        logro_obj.status=False
        logro_obj.save()
        return Response({'message':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)

    def get(self,request):
            lista_list = Logro.objects.all()
            serializer = LogroSerializer(lista_list, many=True)
            
            return Response(serializer.data)

class RandomLogro(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
    
        user_logros = Logro.objects.filter(user_id=request.user)
        otros_logros = Logro.objects.exclude(user_id=request.user)
        
        random_user_logro = random.choice(user_logros) if user_logros.exists() else None
        random_other_logros = otros_logros.order_by('?')[:10]  # Cambia 10 al número deseado
        
        user_logro_data = {
            "titulo": random_user_logro.titulo,
            "descripcion": random_user_logro.descripcion,
            "user": random_user_logro.user_id.username if random_user_logro else None  # Ejemplo de cómo obtener el nombre de usuario
        } if random_user_logro else {}

        other_logros_data = [
            {
                "title": logro.titulo,
                "description": logro.descripcion,
                "user": logro.user_id.username            
            }
            for logro in random_other_logros
        ]
        
        return Response({
            "user_logro": user_logro_data,
            "other_logros": other_logros_data
        })