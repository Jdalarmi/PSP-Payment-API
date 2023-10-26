from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from api.serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

@api_view(['POST'])
def login(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()    
    return Response(serializer.data)