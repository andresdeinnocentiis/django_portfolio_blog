from rest_framework import serializers
from .models import Post, Review, Comment, Like

class PostSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(source='get_likes_count', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

















