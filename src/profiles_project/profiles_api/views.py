from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from . import serializers, models, permissions
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

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


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return hello message"""
        a_viewset = [
            'Uses list, create, retrieve, update, partial_update',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'hello', 'a_viewset':  a_viewset})

    def create(self, request):
        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})

class UserProfileViewset(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewset(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Create and validate a token."""
        return ObtainAuthToken().post(request)
