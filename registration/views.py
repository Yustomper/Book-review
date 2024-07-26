from django import forms
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreationFormWithEmail,ProfileForm,EmailForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile

class SignupView(generic.CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignupView, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Nombre de usuario'
        })
        form.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Email'
        })
        form.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Ingrese su contraseña'
        })
        form.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Repita la contraseña'
        })
        return form

@method_decorator(login_required,name = 'dispatch')
class ProfileUpdate(generic.UpdateView):
    form_class =ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile,created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    def form_valid(self, form):
        if 'avatar' in self.request.FILES:
            form.instance.avatar = self.request.FILES['avatar']
        return super().form_valid(form)
    
@method_decorator(login_required,name = 'dispatch')
class EmailUpdate(generic.UpdateView):
    form_class =EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        return self.request.user
   
    def get_form(self,form_class=None):
        form = super(EmailUpdate, self).get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Email'})
        return form