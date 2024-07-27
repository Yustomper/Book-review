from django.views import generic
from django.db.models import Q
from books.models import Book, Autor

class SearchResultsView(generic.TemplateView):
    template_name = 'search/search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query:
            books = Book.objects.filter(Q(title__icontains=query))
            authors = Autor.objects.filter(Q(name__icontains=query))
            context['books'] = books
            context['authors'] = authors
        return context
