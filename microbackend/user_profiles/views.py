from django.shortcuts import render
from rest_framework import generics
from serializers import UserSerializer
from rest_framework.response import Response
# Create your views here.

class RegisterTest(generics.GenericAPIView):
    serializer_class = UserSerializer
    name = 'register'
    def post(self, request, *args, **kwargs):
        
        return Response({
            'token': {
                "access": "aodjfoadjfoadjf34235fa",
                "refresh": "dfjoiajdfiaipfapfoaopfpoa"
            }
        })
    def get(self, request, *args, **kwargs):
        return Response({
            'token': {
                "access": "aodjfoadjfoadjf34235fa",
                "refresh": "dfjoiajdfiaipfapfoaopfpoa"
            }
        })