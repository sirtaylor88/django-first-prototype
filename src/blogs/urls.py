from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

app_name = "articles"
urlpatterns = [
    path("", ArticleListView.as_view(), name="article-index"),
    path("new/", ArticleCreateView.as_view(), name="article-new"),
    path("<int:id>/", ArticleDetailView.as_view(), name="article-show"),
    path("<int:id>/edit/", ArticleUpdateView.as_view(), name="article-edit"),
    path("<int:id>/delete/", ArticleDeleteView.as_view(), name="article-delete")
]
