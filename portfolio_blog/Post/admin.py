from django.contrib import admin
from .models import Post, Comment, Review, Like

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'caption', 'rating', 'likes', 'num_reviews', 'tech_used', 'created_at', 'updated_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'review_id', 'parent_id', 'user_username', 'likes', 'created_at']

    
    def user_username(self, obj):
        return obj.user.username
    
   

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_id', 'post_title', 'user_username', 'rating', 'likes', 'created_at']
    
    def post_title(self, obj):
        return obj.post.title
    
    post_title.short_description = 'Post Title'  
    
    def user_username(self, obj):
        if obj.user:
            return obj.user.username
        elif obj.anonymous_user:
            return obj.anonymous_user.name
        
    post_title.short_description = 'Post Title' 

class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_title', 'user_username', 'created_at']
    
    def post_title(self, obj):
        return obj.post.title
    
    post_title.short_description = 'Post Title'  
    
    def user_username(self, obj):
        return obj.user.username
    
    post_title.short_description = 'Post Title' 


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Like, LikeAdmin)

