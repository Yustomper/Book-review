from django.db import models

# Create your models here.

class Autor(models.Model):
    name = models.TextField(max_length=200,verbose_name='nombre')
    bio = models.TextField(max_length=200)
    date_birth=models.DateField( auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name