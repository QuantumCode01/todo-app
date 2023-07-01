from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Task(models.Model):
    name=models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    title=models.CharField(max_length=250,unique=True)
    complete=models.BooleanField()
    created=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(null=False)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("update", kwargs={"slug": self.slug}) 
   
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    
    class Meta:
        ordering=['created']
        
    