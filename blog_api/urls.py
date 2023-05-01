from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

router = DefaultRouter()
router.register('', PostList, basename='post')
router.register('blog/post', BlogList, basename='blog_list')
urlpatterns = router.urls


