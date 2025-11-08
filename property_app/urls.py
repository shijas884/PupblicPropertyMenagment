from django.urls import path
from property_app.views import LoginUserView

urlpatterns = [
    path('login/', LoginUserView.as_view()),

]
    