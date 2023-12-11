from django.urls import path
from .views import TagListCreateView, TagDetailUpdateDeleteView, CategoryListCreateView, CategoryDetailUpdateDeleteView, ArticleListCreateView, ArticleRetrieveUpdateDestroyView

urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagDetailUpdateDeleteView.as_view(), name='tag-detail-update-delete'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailUpdateDeleteView.as_view(), name='category-detail-update-delete'),
    path('articles/', ArticleListCreateView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleRetrieveUpdateDestroyView.as_view(), name='article-detail'),
]

