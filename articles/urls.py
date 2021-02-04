from django.urls import path
from .views import (ArticleListView,ArticleUpdateView, ArticleDetailView,ArticleDeleteView,ArticleCreateView)


urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_list'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='articles_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='articles_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='articles_delete'),
     path('new', ArticleCreateView.as_view(), name='articles_new'),
]