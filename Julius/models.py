from django.db import models
from django.db.models.base import Model, ModelBase
from django.db.models.deletion import CASCADE

# Create your models here.
#HOME SECTION


class Home(models.Model):
    name  = models.CharField(max_length= 200)
    greeting_1 = models.CharField(max_length=5)
    greeting_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to ='picture/')
    #save time when modified
    updated  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
#ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=200)
    career = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to = 'picture/')
    
    updated  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.career
    
class Profile(models.Model):
    about = models.ForeignKey(About,on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length= 1000)
    
#SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'skills'
        
class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=200)
    
#PORTFOOLIO SECTION

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio')
    link = models.URLField(max_length=1000)
    
    def __str__(self):
        return f'Portfolio {self.id}' 