from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=99999, decimal_places=2, default=None)
    redactor = models.ForeignKey('Redactor', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.title


class Redactor(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
