from django.urls import path
from .views import book_list_view, BookAddView, book_delete_view


urlpatterns = [
    path('', book_list_view, name='home'),
    path('add/', BookAddView.as_view(), name='add'),
    path('delete/<int:pk>/', book_delete_view, name='delete'),

]
