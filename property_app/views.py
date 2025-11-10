from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status

from property_app.models import LoginUser
from property_app.serializers import RegisterUserSerializer,LoginUserSerializer



class RegisterUserView(CreateAPIView):

    serializer_class = RegisterUserSerializer
    
    def post(self,request):
        reg_seriaizer = RegisterUserSerializer(data=request.data)
        if reg_seriaizer.is_valid():
            user = reg_seriaizer.save()
            seriaized_data = self.get_serializer(user).data

            return Response(data=seriaized_data)
        else:
            return Response(status=400,data = reg_seriaizer.errors)



class LoginUserView(APIView):
    
    def post(self,request):

        log_serializer = LoginUserSerializer(data=request.data)

        if log_serializer.is_valid():
            return Response(
                {
                    "access" : log_serializer.validated_data["access"],
                    "refresh" : log_serializer.validated_data["refresh"],
                    "username" : log_serializer.validated_data['user'].username
                } ,
                status=status.HTTP_200_OK
            )
        return Response(log_serializer.errors,status=status.HTTP_400_BAD_REQUEST)





                