from django.urls import path
from .views import BookFormView,BookListView,BookDetailView,BookUpdateView,BookDeleteView, CommentCreateView,HomeView

urlpatterns = [
    
    path('',HomeView.as_view(),name='home'),
    path('books/',BookListView.as_view(),name='list_book'),
    path('books/books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/<int:book_id>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('books/add/',BookFormView.as_view(),name='books'),
    path('books/update/<int:pk>',BookUpdateView.as_view(),name='update'),
    path('books/delete/<int:pk>',BookDeleteView.as_view(),name='delete')
    
]
