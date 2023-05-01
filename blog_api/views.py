from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from blog.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, IsAuthenticated, AllowAny


class PostCanBeChangedByOnlyUser(BasePermission):
    message = 'Editing post is restricted to only the author only'

    def has_object_permission(self, view, obj, request):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


# class PostList(generics.ListCreateAPIView):
#     permission_class=[IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class=PostSerializer

# class PostDetails(generics.RetrieveUpdateDestroyAPIView, PostCanBeChangedByOnlyUser):
#     permission_class=[PostCanBeChangedByOnlyUser]
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer

class BlogList(viewsets.ViewSet):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()

    def list(self, request):
        serializer = PostSerializer(self.queryset, many=True)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        single_article = get_object_or_404(self.queryset, pk=pk)
        serializer_class = PostSerializer(single_article)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        single_blog = get_object_or_404(self.queryset, pk=pk)
        single_blog.delete()
        return Response(status=status.HTTP_100_CONTINUE)


class PostList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        slug = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=slug)

    def get_queryset(self):
        return Post.objects.all()
