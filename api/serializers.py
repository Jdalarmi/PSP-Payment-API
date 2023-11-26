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
    card_number = serializers.CharField(max_length=19, default='2222-2222-2222-2222')
    cvv = serializers.CharField(max_length=3, default='123')

    class Meta:
        model = Transaction
        fields = '__all__'
        
    def validate_card_number(self, attrs):
        if len(attrs) > 19 or len(attrs) < 19:
            raise serializers.ValidationError('O cartão não existe pois possue mais de 18 caracteres, incluindo separadores', code=status.HTTP_400_BAD_REQUEST)
        if attrs[4] != '-' and attrs[9] != '-' and attrs[14] != '-':
            raise serializers.ValidationError("cartão inválido", code=status.HTTP_400_BAD_REQUEST)
        for letra in attrs:
            if letra == '-':
                continue
            if not letra.isdigit():
                raise serializers.ValidationError("cartão inválido, contem letras", code=status.HTTP_400_BAD_REQUEST)

        return attrs
    
    def validate_cvv(self, attrs):
        if len(attrs) != 3:
            raise serializers.ValidationError('O cartão não existe pois possue mais de 18 caracteres, incluindo separadores', code=status.HTTP_400_BAD_REQUEST)
        if not attrs.isdigit():
            raise serializers.ValidationError('O CVV precisá ser 3 digitos', code=status.HTTP_400_BAD_REQUEST) 
        return attrs
    
        


class PayablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payables
        fields = '__all__'