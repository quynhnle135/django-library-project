from django.urls import path
from . import views


urlpatterns = [
    path("books/", views.BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    path("books/add/", views.BookAddView.as_view(), name="book-add"),
    path("books/<int:pk>/update/", views.BookUpdateView.as_view(), name="book-update"),
    path("books/<int:pk>/delete/", views.BookDeleteView.as_view(), name="book-delete"),
]