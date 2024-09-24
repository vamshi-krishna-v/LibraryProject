from django.contrib import admin
from .models import Book, Borrowing

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'isbn', 'borrowed')
    list_filter = ('borrowed',)

class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'borrow_date', 'return_date')

admin.site.register(Book, BookAdmin)
admin.site.register(Borrowing, BorrowingAdmin)