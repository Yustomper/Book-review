from django.contrib import admin
from .models import Book,Category

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','autor')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')

admin.site.register(Book,BookAdmin)
admin.site.register(Category)