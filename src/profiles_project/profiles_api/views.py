from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status

# Create your views here.

class HelloAPIView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP method as function (get, put, post, patch, delete)',
            'It is similar to a django view',
            'Gives you most control overyour logic',
            'mapped manually to URLs'
        ]

        return Response({'message': 'Hello World!', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'Hello {0}'.format(name)
            return Response({'message': msg})
        else:
            return Response(
            serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Updating an object"""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """only updates fields provided in request"""
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        return Response({'method': 'delete'})
