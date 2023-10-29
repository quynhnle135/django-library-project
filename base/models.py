from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    summary = models.TextField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.title

