from django.urls import path

from property_app.views import (RegisterUserView,LoginUserView,
                                StateCreateView,StateListView,
                                StateDetailView,DistrictListView,
                                DistrictCreateView,DistrictDetailview,
                                TalukListView,TalukCreateView,TalukDetailView,
                                PanchayatListView,PanchayatCreateView,PanchayatDetailView


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

    


   
]
    