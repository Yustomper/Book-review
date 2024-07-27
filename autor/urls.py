from django.urls import path
from .views import AutorListView, FollowAuthorView

urlpatterns = [
    path('', AutorListView.as_view(), name='autores'),
    path('follow/<int:author_id>/', FollowAuthorView.as_view(), name='follow_author'),
]
