from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField()
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    tech_used = models.TextField()
    num_reviews = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    github_link = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.title



class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return str(self.id)
    

class Comment(models.Model):
    review = models.ForeignKey(Review, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE) # Esto es para autorreferenciarse y poder ser comentados a sí mismos con el id del comment o review padre

    def __str__(self) -> str:
        return str(self.id)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.id)