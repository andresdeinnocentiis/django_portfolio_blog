from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    years_exp = models.FloatField(default=0.0)
    validations = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name

class Study(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    institution_link = models.CharField(max_length=100)
    certificate_link = models.CharField(max_length=100)
    validations = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name
    
class Validation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, null=True, blank=True, on_delete=models.CASCADE)
    study = models.ForeignKey(Study, null=True, blank=True, on_delete=models.CASCADE)