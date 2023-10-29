from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.BookListAPIView.as_view()),
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view()),
]