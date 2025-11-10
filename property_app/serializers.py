from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from property_app.models import LoginUser


class RegisterUserSerializer(ModelSerializer):

    class Meta:
        model = LoginUser
        fields = ['id','username','password','role_type']
        
    def create(self, validated_data):
        user = LoginUser.objects.create_user( **validated_data )
        return user
    

class LoginUserSerializer(Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if not username or not password:
            raise serializers.ValidationError("Both username and password " 
                                              "are required")
        
        user = authenticate(username=username,password=password)
        if not user:
            raise serializers.ValidationError("Invalid username or password")
            
        # Jwt tokens
        refresh = RefreshToken.for_user(user)
        attrs['refresh'] = str(refresh)
        attrs['access'] = str(refresh.access_token)
        attrs['user'] = user
        return attrs
            

        