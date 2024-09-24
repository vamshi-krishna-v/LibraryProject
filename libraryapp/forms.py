from django import forms
from .models import Book, Borrowing

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date', 'isbn')

class BorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ('book', 'borrower', 'borrow_date', 'return_date')