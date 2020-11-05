from rest_framework import generics
from bookpubl.serializers import BookDetailSerializer, BookListSerializer
from bookpubl.models import Book


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookDetailSerializer

class BookListView(generics.ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()
   
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()