from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Like
from .serializers import LikeSerializer


class LikeCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        serializer = LikeSerializer(data=data)
        if serializer.is_valid():
            like = serializer.save(user=request.user)
            return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, like_id):
        like_obj = get_object_or_404(Like, pk=like_id)
        like_obj.status=False
        like_obj.save()
        return Response({'message':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)
