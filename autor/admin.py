from django.contrib import admin
from .models import Autor

# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Autor,AutorAdmin)