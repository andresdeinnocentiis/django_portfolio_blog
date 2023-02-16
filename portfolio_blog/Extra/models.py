from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True,upload_to=f'tech_images')
    years_exp = models.FloatField(default=0.0)
    validations = models.IntegerField(default=0)
    
    def get_validations_count(self):
        return Validation.objects.filter(technology=self).count()

    @property
    def validations(self):
        return self.get_validations_count()
    
    def __str__(self) -> str:
        return self.name

class Study(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True,upload_to=f'study_images')
    description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    institution_link = models.CharField(max_length=100,null=True, blank=True)
    certificate_link = models.CharField(max_length=100,null=True, blank=True)
    validations = models.IntegerField(default=0)
    
        
    def get_validations_count(self):
        return Validation.objects.filter(study=self).count()

    @property
    def validations(self):
        return self.get_validations_count()
    
    def __str__(self) -> str:
        return self.name
    
class Validation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    anonymous_identifier = models.CharField(max_length=255, null=True, blank=True)
    technology = models.ForeignKey(Technology, null=True, blank=True, on_delete=models.CASCADE)
    study = models.ForeignKey(Study, null=True, blank=True, on_delete=models.CASCADE)