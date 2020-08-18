from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from .models import Comment, Post, Group,Follow
from .serializers import CommentSerializer, PostSerializer, GroupSerializer,FollowSerializer
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_fields = ('post', 'id')


    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['id'])
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['id'])
        queryset = Comment.objects.filter(post=post)
        return queryset

class GroupListView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowListView(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=user__username', '=following__username')

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)