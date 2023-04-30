from django.urls import path
from .views import *

app_name="users"

urlpatterns = [
  path('register/', RegisterUser.as_view(),name="register_user")
   
]