from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
# class BookDetailAPIView(RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'slug'
    
 
class BookDetailAPIView(APIView):
    def get(self, request, slug):
        try:
            book = Book.objects.get(slug=slug)
            serializer_data = BookSerializer(book).data
            data = {
                'status':'successfull',
                'book':serializer_data,
                }
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(data={
                'status':'False',
                'message':'Data is not found',
                }, status=status.HTTP_404_NOT_FOUND )
    
class BookDeleteAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'
    

class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'

class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

