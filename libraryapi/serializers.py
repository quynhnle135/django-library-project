from rest_framework import serializers
from base.models import Book


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    publication_date = serializers.DateField()
    summary = serializers.CharField(allow_blank=True, allow_null=True)
    review = serializers.CharField(allow_blank=True, allow_null=True)
    rating = serializers.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        model = Book
        fields = "__all__"
