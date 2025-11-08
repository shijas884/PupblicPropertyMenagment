from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from property_app.models import LoginUser
from property_app.serializers import CreateLoginSerializer, LoginUserSerializer


class LoginUserView(CreateAPIView):

    serializer_class = LoginUserSerializer

    def post(self,request):
        serializer = CreateLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            serialized_data = self.get_serializer(user).data

            return Response(data=serialized_data)
        else:
            return Response(status=400, data=serializer.errors)
        
 