from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

@api_view(['GET', 'POST'])
def apiTest(request):
    return Response({'message': 'Hello, World!'}, status=status.HTTP_200_OK)

class testapiView(APIView):
    def get(self, request):
        author = request.GET['author']
        
        if(author):
            return Response({'message': 'Hello, World! ' + author}, status=status.HTTP_200_OK)
        
        return Response({'message': 'Hello, World!'}, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response({"title": request.data.get('title')}, status=status.HTTP_201_CREATED)

class testapi(APIView):
    def get(self, request, pk):      
        
        return Response({'message': 'Hello, World! ' + str(pk)}, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        return Response({"title": request.data.get('title')}, status=status.HTTP_201_CREATED)

