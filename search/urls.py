from django.urls import path
from search.views import SearchResultsView


urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search'),
]
