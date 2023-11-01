from base.models import Book
from .serializers import BookSerializer
from rest_framework import generics


# Create your views here.
class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookAddAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer