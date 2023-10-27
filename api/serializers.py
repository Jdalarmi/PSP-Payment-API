from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import status

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

    