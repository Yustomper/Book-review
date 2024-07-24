from django.db import models

# Create your models here.
class Autor(models.Model):
    name = models.CharField(max_length=200,verbose_name='Nombre')
    bio = models.TextField(verbose_name='Biografia')
    date_birth = models.DateField(auto_now_add=True,verbose_name='Fecha de cumpleaños')

    def __str__(self):
        return self.name