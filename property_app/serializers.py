from rest_framework.serializers import ModelSerializer

from property_app.models import LoginUser


class CreateLoginSerializer(ModelSerializer):

    class Meta:
        model = LoginUser
        fields = ["username", "password", "role_type"]

    def create(self, validated_data):
        user = LoginUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            role_type=validated_data['role_type']
            )
        return user


class LoginUserSerializer(ModelSerializer):

    class Meta:
        model = LoginUser
        fields = '__all__'