from django.contrib import admin
from django.urls import path, include
from bookpubl.views import BookCreateView, BookListView, BookDetailView

app_name = 'book'
urlpatterns = [
    path('book/create/', BookCreateView.as_view()),
    path('all/', BookListView.as_view()),
    path('book/detail/<int:pk>/', BookDetailView.as_view())
]