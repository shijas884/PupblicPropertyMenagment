from django.urls import path

from property_app.views import (RegisterUserView,LoginUserView,
                                StateCreateView,StateListView,
                                StateDetailView,DistrictListView,
                                DistrictCreateView,DistrictDetailview,
                                TalukListView,TalukCreateView,TalukDetailView,
                                PanchayatListView,PanchayatCreateView,PanchayatDetailView,
                                PropertyTypeListView,PropertyTypeCreateView,PropertyTypeDetailView,
                                PublicPropertyListView,PublicPropertyCreateView,PublicPropertyDetailView,
                                AttributeListView,AttributeCreateView,AttributeDetailView,
                                PropertyDetailsListView,PropertyDetailsCreateView,PropertyDetailsDetailView

                               )



urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('login/', LoginUserView.as_view()),

    path('statelist/', StateListView.as_view()),
    path('statecreate/', StateCreateView.as_view()),
    path('statedetail/<int:pk>/', StateDetailView.as_view()),

    path('discritlist/', DistrictListView.as_view()),
    path('discritcreate/', DistrictCreateView.as_view()),
    path('discritdetail/<int:pk>/', DistrictDetailview.as_view()),

    path('taluklist/', TalukListView.as_view()),
    path('talukcreate/', TalukCreateView.as_view()),
    path('talukdetail/<int:pk>/', TalukDetailView.as_view()),

    path('Panchayatlist/', PanchayatListView.as_view()),
    path('Panchayatcreate/', PanchayatCreateView.as_view()),
    path('Panchayatdetail/<int:pk>/', PanchayatDetailView.as_view()),

    path('propertytypelist/', PropertyTypeListView.as_view()),
    path('propertytypecreate/', PropertyTypeCreateView.as_view()),
    path('propertytypedetail/<int:pk>/', PropertyTypeDetailView.as_view()),

    path('publicpropertylist/', PublicPropertyListView.as_view()),
    path('publicpropertycreate/', PublicPropertyCreateView.as_view()),
    path('publicpropertydetail/<int:pk>/', PublicPropertyDetailView.as_view()),

    path('attributelist/', AttributeListView.as_view()),
    path('attributecreate/', AttributeCreateView.as_view()),
    path('attributedetail/<int:pk>/', AttributeDetailView.as_view()),

    path('propertydetailslist/', PropertyDetailsListView.as_view()),
    path('propertydetailscreate/', PropertyDetailsCreateView.as_view()),
    path('propertydetailsdetail/<int:pk>/', PropertyDetailsDetailView.as_view()),
   
]
    