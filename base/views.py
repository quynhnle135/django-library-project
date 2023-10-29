from django.views import generic
from .models import Book
from django.urls import reverse_lazy


# Create your views here.
class BookListView(generic.ListView):
    model = Book
    context_object_name = "books"
    template_name = "base/book_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()

        title = self.request.GET.get("title")
        author = self.request.GET.get("author")
        min_rating = self.request.GET.get("min_rating")
        publication_date = self.request.GET.get("publication_date")

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)
        if publication_date:
            queryset = queryset.filter(publication_date=publication_date)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = context["books"].count()
        # context["search-area"] = self.request.GET.get("search-area")
        return context


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
