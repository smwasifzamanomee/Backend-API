from django.shortcuts import render
from rest_framework.response import Response
from .serializers import LittleLemonSerializer
from .models import Menu
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class LittleLemonView(APIView):
    def get(self, request):
        lemons = Menu.objects.all()
        serializer = LittleLemonSerializer(lemons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = LittleLemonSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)