from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label="nombre",required=True,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Escribe tu Nombre'}
    ),min_length=3,max_length=100)
    email=forms.EmailField(label="email",required=True,widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Escribe tu Email'}),min_length=3,max_length=100)
    content=forms.CharField(label="contenido",required=True,widget=forms.Textarea(
        attrs={'class':'form-control','rows':3,'placeholder':'Escribe tu Mensaje'}
    ),min_length=10,max_length=1000)
        
    