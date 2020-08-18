from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Post, Comment, Group, Follow


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
            fields = ('user', 'following')
            model = Follow
            validators = [
                UniqueTogetherValidator(
                    queryset=Follow.objects.all(),
                    fields=('user', 'following')
                )
            ]