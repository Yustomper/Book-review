from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Autor(models.Model):
    name = models.TextField(max_length=200,verbose_name='nombre')
    bio = models.TextField(max_length=200)
    date_birth=models.DateField( auto_now=False, auto_now_add=False)
    photo = models.ImageField(upload_to='authors/photos/', null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='following', through='Follow')

    def __str__(self):
        return self.name
    
class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'author')

    def __str__(self):
        return f"{self.user} follows {self.author}"