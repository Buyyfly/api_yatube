from rest_framework.routers import SimpleRouter
from django.urls import include, path
import djoser.urls.jwt
import djoser.urls
from .views import PostViewSet, GroupViewSet, CommentViewSet


router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('auth/', include(djoser.urls)),
    path('auth/', include(djoser.urls.jwt)),
]
