
from django.shortcuts import render
from rest_framework.decorators import api_view
from api.serializers import TransactionSerializer, UserSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.models import User


@swagger_auto_schema(method='post', request_body=UserSerializer)
@api_view(['POST'])
def login(request):
    serializer = UserSerializer(data=request.data)
    username = request.data['username']

    if serializer.is_valid():
        serializer.save()
        return Response(f'Usuario {username} criado com sucesso!!!')
    else:
        return Response(serializer.errors)   

@swagger_auto_schema(method='post', request_body=TransactionSerializer)
@api_view(['POST'])
def register_transaction(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Transacao realizada com sucesso!!!')
    else:
        return Response(serializer.errors)