from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    synopsis = models.TextField()

    def __str__(self):
        return self.title
