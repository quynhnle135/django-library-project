from django.urls import path
from . import views


urlpatterns = [
    path("", views.BookListView.as_view(), name="book-list"),
    path("<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    path("add/", views.BookAddView.as_view(), name="book-add"),
    path("<int:pk>/update/", views.BookUpdateView.as_view(), name="book-update"),
    path("<int:pk>/delete/", views.BookDeleteView.as_view(), name="book-delete"),
]