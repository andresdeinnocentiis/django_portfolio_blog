from rest_framework import serializers
from .models import Post, Review, Comment, Like

class PostSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(source='get_likes_count', read_only=True)
    num_reviews = serializers.IntegerField(source='get_reviews_count', read_only=True)
    rating = serializers.DecimalField(source='get_average_rating', read_only=True, max_digits=5, decimal_places=2)
    class Meta:
        model = Post
        fields = '__all__'
        
    def get_likes(self, obj):
        return obj.likes
    def get_num_reviews(self, obj):
        return obj.num_reviews
    def get_rating(self, obj):
        return obj.rating

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

















