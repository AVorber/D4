from django.contrib import admin
from p_library.models import Book, Author, Redactor


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count', 'redactor')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):

    @staticmethod
    def list_book(obj):
        books = obj.book_set.all()
        lst = []
        for book in books:
            lst.append(book.title)

        return lst

    list_display = ('name', 'list_book')
    fields = ('name', )
