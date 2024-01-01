from django.urls import path
from .views import BookCreate, BookList, BookDetail, BookUpdate, BookDelete

urlpatterns = [
    path('', BookList.as_view()),
    path('book_create', BookCreate.as_view()),
    path('book_list', BookList.as_view()),
    path('book_detail/<pk>/', BookDetail.as_view()),
    path('book_update/<pk>/', BookUpdate.as_view()),
    path('book_delete/<pk>/', BookDelete.as_view()),
]
