from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(null=True)
    isbn = models.CharField(max_length=20, unique=True)
    borrowed = models.BooleanField(default=False)
    def  __str__(self):
      return self.title

class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.CharField(max_length=100)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    
    def  __str__(self):
      return self.book.title + ' borrowed by ' + self.borrower

