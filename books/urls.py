from django.urls import path
from .views import BookFormView,BookListView,BookDetailView,BookUpdateView,BookDeleteView, CommentCreateView

urlpatterns = [
    
    path('',BookListView.as_view(),name='list_book'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('<int:book_id>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('add/',BookFormView.as_view(),name='books'),
    path('update/<int:pk>',BookUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',BookDeleteView.as_view(),name='delete')
    
]
