from django.shortcuts import render, redirect
from .models import Book, Borrowing
from .forms import BookForm, BorrowingForm

def base(request):
    Books=Book.objects.all()
    return render(request,'libraryapp/base.html',{'books':Books})
    


def book_list(request):
    books = Book.objects.all()
    return render(request, 'libraryapp/book_list.html', {'books': books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'libraryapp/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'libraryapp/add_book.html', {'form': form})

def borrow_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BorrowingForm(request.POST)
        if form.is_valid():
            form.save()
            book.borrowed = True
            book.save()
            return redirect('book_list')
    else:
        form = BorrowingForm()
    return render(request, 'libraryapp/borrow_book.html', {'form': form, 'book': book})

def return_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.borrowed = False
    book.save()
    return redirect('book_list')