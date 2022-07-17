from rest_framework.routers import SimpleRouter
from django.urls import include, path
from .views import PostViewSet, GroupViewSet, CommentViewSet


router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('group', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
