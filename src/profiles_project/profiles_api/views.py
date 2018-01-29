from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloAPIView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP method as function (get, put, post, patch, delete)',
            'It is similar to a django view',
            'Gives you most control overyour logic',
            'mapped manually to URLs'
        ]

        return Response({'message': 'Hello World!', 'an_apiview': an_apiview})
        
