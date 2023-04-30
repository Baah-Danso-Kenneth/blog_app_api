from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, IsAuthenticated


class PostCanBeChangedByOnlyUser(BasePermission):
    message='Editing post is restriced to only the author only'

    def has_object_permission(self,view,obj,request):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class=PostSerializer

class PostDetails(generics.RetrieveUpdateDestroyAPIView, PostCanBeChangedByOnlyUser):
    permission_class=[PostCanBeChangedByOnlyUser]
    queryset=Post.objects.all()
    serializer_class=PostSerializer
