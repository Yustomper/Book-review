from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import BookForm,CommentForm
from .models import Book,Comment
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(generic.TemplateView):
    template_name = 'books/home.html'


class BookFormView(LoginRequiredMixin,generic.FormView):
    template_name = 'books/add_book.html'
    form_class = BookForm
    success_url = reverse_lazy('list_book')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/list_book.html'
    context_object_name = 'books'
    paginate_by = 8  

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(book=self.object)
        context['form'] = CommentForm()  # Agrega el formulario al contexto
        return context


class BookUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Book
    fields = ['title','autor','description','image','category','price']
    template_name_suffix = '_update_form'


    def get_success_url(self):
        return reverse_lazy('update',args=[self.object.id])+'?ok'



class BookDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Book
    success_url = reverse_lazy('list_book')

class CommentCreateView(generic.FormView):
    form_class = CommentForm

    def form_valid(self, form):
        book = get_object_or_404(Book, pk=self.kwargs['book_id'])
        comment = form.save(commit=False)
        comment.book = book
        comment.user = self.request.user
        comment.save()
        return redirect('book_detail', pk=book.pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial']['book'] = get_object_or_404(Book, pk=self.kwargs['book_id'])
        return kwargs