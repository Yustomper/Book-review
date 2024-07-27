from django import forms
from .models import Book, Category,Comment
from autor.models import Autor

class BookForm(forms.Form):
    title = forms.CharField(max_length=200, label='Título', widget=forms.TextInput(attrs={'class': 'w-full border border-black p-2 rounded'}))
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), label='Autor', widget=forms.Select(attrs={'class': 'w-full border border-black p-2 rounded'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-full border border-black p-2 rounded'}), label='Descripción')
    image = forms.ImageField(label='Imagen', required=False, widget=forms.ClearableFileInput(attrs={'class': 'w-full border border-black p-2 rounded'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Categoría', widget=forms.Select(attrs={'class': 'w-full border border-black p-2 rounded'}))
    price = forms.DecimalField(max_digits=6, decimal_places=2, label='Precio', widget=forms.NumberInput(attrs={'class': 'w-full border border-black p-2 rounded'}))  # Nuevo campo para el precio

    def save(self):
        return Book.objects.create(
            title=self.cleaned_data['title'],
            autor=self.cleaned_data['autor'],
            description=self.cleaned_data['description'],
            image=self.cleaned_data.get('image'),  
            category=self.cleaned_data['category'],
            price=self.cleaned_data['price'] ,
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full p-2 border border-gray-300 rounded-lg',
                'placeholder': 'Escribe tu comentario aquí...'
            }),
            'rating': forms.Select(choices=[(i, f"{i} estrella{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg'
            }),
        }