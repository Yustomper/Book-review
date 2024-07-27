from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from .models import Profile

class SignupView(generic.CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignupView, self).get_form()
        # (Tu código existente para estilizar el formulario)
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(generic.UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

@method_decorator(login_required, name='dispatch')
class EmailUpdate(generic.UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # (Tu código existente para estilizar el formulario)
        return form

def profile_detail(request, username):
    profile = Profile.objects.get(user__username=username)
    return render(request, 'registration/profile_detail.html', {'profile': profile})