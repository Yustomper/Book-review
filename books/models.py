from django.db import models
from autor.models import Autor

    # Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=200,verbose_name='Titulo')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(null=True,blank=True,upload_to='libros/',verbose_name='Imagen')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,verbose_name='Categoria')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Precio', default=0.00)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title