from django import forms
from django.forms import ModelForm
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import status

from api.models import Payables, Transaction
from core import settings

class UserSerializer(serializers.ModelSerializer):
    def validate(self, value):
        username = value['username']
        password = value['password']
        if username == password:
            raise serializers.ValidationError('Campos iguais', code=status.HTTP_400_BAD_REQUEST)
        return value
    
    def validate_username(self, attrs):
        if len(attrs) < 2:
            raise serializers.ValidationError('username menor que 2 caracteres', code=status.ba)
        return attrs
    
    def validate_password(self, attrs):
        if len(attrs) < 6:
            raise serializers.ValidationError('Senha menor que 6 digitos', code=status.HTTP_400_BAD_REQUEST)
        return attrs
    def validate_card_number(self, attrs):
        if len(attrs) > 18:
            raise serializers.ValidationError('O cartão não existe pois possue mais de 18 caracteres, incluindo separadores', code=status.HTTP_400_BAD_REQUEST)
        return attrs

    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            password = validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username','password']


class TransactionSerializer(serializers.ModelSerializer):
    card_number = serializers.CharField(default='2222-2222-2222-2222')

    class Meta:
        model = Transaction
        fields = '__all__'
   

class PayablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payables
        fields = '__all__'
    class Meta:
        model = Payables
        fields = '__all__'