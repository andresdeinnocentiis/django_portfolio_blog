from django.db import models
from django.contrib.auth.models import User
from UserProfile.models import AnonymousUser, UserProfile

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to=f'posts_images')
    description = models.TextField()
    tech_used = models.TextField()
    developed_for = models.CharField(max_length=100, null=True, blank=True, default="")
    developed_for_link = models.CharField(max_length=100, null=True, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, default="Completed")
    updated_at = models.DateTimeField(auto_now=True)
    github_link = models.CharField(max_length=100, null=True, blank=True)
    website_link = models.CharField(max_length=100, null=True, blank=True)
    
    # Here I add calculated fields (likes, num_reviews, rating):
    
    def get_likes_count(self):
        return Like.objects.filter(post=self).count()
    @property
    def likes(self):
        return self.get_likes_count()
    
    def get_reviews_count(self):
        return Review.objects.filter(post=self).count()
    @property
    def num_reviews(self):
        return self.get_reviews_count()
    
    def get_average_rating(self):
        reviews = Review.objects.filter(post=self)
        count = reviews.count()
        if count == 0:
            return 0
        total_rating = sum([r.rating for r in reviews])
        return total_rating / count
    @property
    def rating(self):
        return self.get_average_rating()
    

    likes.fget.short_description = 'Likes'
    num_reviews.fget.short_description = 'Reviews'
    rating.fget.short_description = 'Rating'
    
    def __str__(self) -> str:
        return self.title



class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    anonymous_user = models.ForeignKey(AnonymousUser, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_likes_count(self):
        return Like.objects.filter(review=self).count()

    @property
    def likes(self):
        return self.get_likes_count()
    
    def get_comments_count(self):
        return Comment.objects.filter(review=self).count()

    @property
    def comments(self):
        return self.get_comments_count()
    
    likes.fget.short_description = 'Likes'
    comments.fget.short_description = 'Comments'
    
    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        unique_together = (('post', 'user'),('post', 'anonymous_user')) # I added this so that a user/anon could leave a single review for each post.
    

class Comment(models.Model):
    review = models.ForeignKey(Review, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    anonymous_user = models.ForeignKey(AnonymousUser, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE) # Esto es para autorreferenciarse y poder ser comentados a sí mismos con el id del comment o review padre

    def get_likes_count(self):
        return Like.objects.filter(comment=self).count()

    @property
    def likes(self):
        return self.get_likes_count()
    
    def get_comments_count(self):
        return Comment.objects.filter(parent=self).count()

    @property
    def comments(self):
        return self.get_comments_count()
    
    likes.fget.short_description = 'Likes'
    comments.fget.short_description = 'Comments'
    
    def __str__(self) -> str:
        return str(self.id)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    anonymous_identifier = models.CharField(max_length=255, null=True, blank=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.id)