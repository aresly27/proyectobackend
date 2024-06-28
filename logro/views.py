from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Logro
from .serializers import LogroSerializer

class LogroView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        data = request.data
        serializer = LogroSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'message':'Creado'}, status=status.HTTP_201_CREATED)