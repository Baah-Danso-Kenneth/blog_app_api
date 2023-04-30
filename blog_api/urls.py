from django.urls import path
from .views import PostList,PostDetails

app_name='blog_api'

urlpatterns = [
  path('',PostList.as_view(), name="listcreate"),
  path('<int:pk>/',PostDetails.as_view(), name="detailcreate")

]
