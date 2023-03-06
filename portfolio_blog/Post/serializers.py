from rest_framework import serializers
from .models import Post, Review, Comment, Like
from UserProfile.models import UserProfile
from UserProfile.serializers import UserProfileSerializer, UserSerializer

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
    user = UserSerializer()
    anonymous_user = serializers.SerializerMethodField()
    likes = serializers.IntegerField(source='get_likes_count', read_only=True)
    comments = serializers.IntegerField(source='get_comments_count', read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'post', 'user', 'anonymous_user','likes', 'comments', 'content', 'rating', 'created_at']
    
    def get_user(self, obj):
        if obj.user:
            return obj.user
        else:     
            return None
        
    
    def get_anonymous_user(self, obj):
        if obj.anonymous_user:
            return {
                'id': obj.anonymous_user.id,
                'anonymous_identifier': obj.anonymous_user.anonymous_identifier,
                'username': obj.anonymous_user.username
            }
        return None
    
class ReviewPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
    
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    anonymous_user = serializers.SerializerMethodField()
    likes = serializers.IntegerField(source='get_likes_count', read_only=True)
    comments = serializers.IntegerField(source='get_comments_count', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        
    def get_user(self, obj):
        if obj.user:
            return {
                'id': obj.user.id,
                'username': obj.user.username,
                'linkedin': obj.user.linkedin,
                'image': obj.user.image if obj.user.image else None
                
            }
        return None
    
    def get_anonymous_user(self, obj):
        if obj.anonymous_user:
            return {
                'id': obj.anonymous_user.id,
                'anonymous_identifier': obj.anonymous_user.identifier,
                'username': obj.anonymous_user.username
            }
        return None

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

















