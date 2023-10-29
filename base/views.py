from django.views import generic
from .models import Book
from django.urls import reverse_lazy


# Create your views here.
class BookListView(generic.ListView):
    model = Book
    context_object_name = "books"
    template_name = "base/book_list.html"


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "base/book_detail.html"


class BookAddView(generic.CreateView):
    model = Book
    fields = "__all__"
    template_name = "base/book_form.html"
    success_url = reverse_lazy("book-list")


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = "__all__"
    template_name = "base/book_update_form.html"
    success_url = reverse_lazy("book-list")


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "base/book_confirm_delete_form.html"
    success_url = reverse_lazy("book-list")
