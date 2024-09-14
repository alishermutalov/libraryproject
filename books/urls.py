from django.urls import path
from .views import (
    BookListAPIView,
    BookDetailAPIView,
    BookDeleteAPIView,
    BookUpdateAPIView,
    BookCreateAPIView
    )

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book_list'),
    path('book/create/', BookCreateAPIView.as_view(), name='book_list'),
    path('detail/<slug:slug>/', BookDetailAPIView.as_view(), name='book_detail'),
    path('delete/<slug:slug>/', BookDeleteAPIView.as_view(), name='book_delete'),
    path('update/<slug:slug>/', BookUpdateAPIView.as_view(), name='book_update'),
]
