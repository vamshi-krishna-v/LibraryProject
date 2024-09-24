from django.urls import path
from . import views
urlpatterns = [
    path('', views.base, name ='base'),
    path('book_list/',views.book_list,name='book_list' ),
    path('add_book/', views.add_book, name='add_book'),
    path('book/<pk>/', views.book_detail, name='book_detail'),
    path('borrow_book/<pk>/', views.borrow_book, name='borrow_book'),
    path('return_book/<pk>/', views.return_book, name='return_book'),
]