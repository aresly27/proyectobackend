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
    
    def put(self, request, logro_id):
        logro_obj = get_object_or_404(Logro, id=logro_id)
        serializer = LogroSerializer(instance=logro_obj, data=request.data, partial=True )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
