from django.urls import reverse_lazy
from django.views import generic
from .forms import BookForm
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin




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




class BookUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Book
    fields = ['title','autor','description','image','category','price']
    template_name_suffix = '_update_form'


    def get_success_url(self):
        return reverse_lazy('update',args=[self.object.id])+'?ok'



class BookDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Book
    success_url = reverse_lazy('list_book')