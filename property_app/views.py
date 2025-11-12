from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,ListAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                    )


from property_app.models import (LoginUser, State, District,
                                 Taluk,Panchayat,PropertyType,
                                 PublicProperty,Attribute,PropertyDetails

                                )
from property_app.serializers import (RegisterUserSerializer,LoginUserSerializer,
                                      StateSerializer,DistrictSeriaizer,TalukSerializer,
                                      PanchayatSerializer,PropertyTypeSeriaizer,PublicPropertySerializer,
                                      AttributeSerializer,PropertyDetailsSerializer
                                      )

from .permissions import IsAdmin,IsWriterOrAdnin,IsViewer


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


# State View 

class StateListView(ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsViewer] 


class StateCreateView(CreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAdmin]

class StateDetailView(RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer 
    permission_classes = [IsAdmin]

# Discrit view

class DistrictListView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSeriaizer
    permission_classes = [IsViewer]


class DistrictCreateView(CreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSeriaizer
    permission_classes = [IsAdmin]

class DistrictDetailview(RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSeriaizer
    permission_classes = [IsAdmin]

# taluk view 

class TalukListView(ListAPIView):
    queryset = Taluk.objects.all()
    serializer_class = TalukSerializer
    permission_classes = [IsViewer]
    

class TalukCreateView(CreateAPIView):
    queryset = Taluk.objects.all()
    serializer_class = TalukSerializer
    permission_classes = [IsAdmin]

class TalukDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Taluk.objects.all()
    serializer_class = TalukSerializer
    permission_classes = [IsAdmin]

    
# panjayath view

class PanchayatListView(ListAPIView):
    queryset = Panchayat.objects.all()
    serializer_class = PanchayatSerializer
    permission_classes = [IsViewer]
    

class PanchayatCreateView(CreateAPIView):
    queryset = Panchayat.objects.all()
    serializer_class = PanchayatSerializer
    permission_classes = [IsAdmin]

class PanchayatDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Panchayat.objects.all()
    serializer_class = PanchayatSerializer
    permission_classes = [IsAdmin]


# PropertyType view 

class PropertyTypeListView(ListAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSeriaizer
    permission_classes = [IsViewer]
    

class PropertyTypeCreateView(CreateAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSeriaizer
    permission_classes = [IsAdmin]

class PropertyTypeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSeriaizer
    permission_classes = [IsAdmin]

# publicproperty views 

class PublicPropertyListView(ListAPIView):
    queryset = PublicProperty.objects.all()
    serializer_class = PublicPropertySerializer
    permission_classes = [IsViewer]
    
class PublicPropertyCreateView(CreateAPIView):
    queryset = PublicProperty.objects.all()
    serializer_class = PublicPropertySerializer
    permission_classes = [IsAdmin]

class PublicPropertyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PublicProperty.objects.all()
    serializer_class = PublicPropertySerializer
    permission_classes = [IsAdmin]


# Attribute view

class AttributeListView(ListAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = [IsViewer]
    
class AttributeCreateView(CreateAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = [IsAdmin]

class AttributeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = [IsAdmin]

# PropertyDetails views

class PropertyDetailsListView(ListAPIView):
    queryset = PropertyDetails.objects.all()
    serializer_class = PropertyDetailsSerializer
    permission_classes = [IsViewer]
    
class PropertyDetailsCreateView(CreateAPIView):
    queryset = Attribute.objects.all()
    serializer_class = PropertyDetailsSerializer
    permission_classes = [IsAdmin]

class PropertyDetailsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PropertyDetails.objects.all()
    serializer_class = PropertyDetailsSerializer
    permission_classes = [IsWriterOrAdnin]

