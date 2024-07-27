from django.views.generic import ListView
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Autor, Follow
from django.views.generic import ListView
from .models import Autor, Follow

class AutorListView(ListView):
    model = Autor
    template_name = 'autor/autores_list.html'
    context_object_name = 'authors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            follow_status = {author.id: Follow.objects.filter(user=user, author=author).exists() for author in context['authors']}
            context['follow_status'] = follow_status
        return context
    
class FollowAuthorView(LoginRequiredMixin, View):
    def post(self, request, author_id):
        author = get_object_or_404(Autor, id=author_id)
        follow, created = Follow.objects.get_or_create(user=request.user, author=author)
        if not created:
            follow.delete()
        return redirect('autores')