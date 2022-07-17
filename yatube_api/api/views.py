from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Comment, Group, Post
from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from .permissions import OwnerOrRead


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, OwnerOrRead]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, OwnerOrRead]

    def get_queryset(self):
        queryset = Comment.objects.all()
        post_id = self.kwargs['post_id']
        if post_id is not None:
            queryset = queryset.filter(post_id=self.kwargs['post_id'])
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
