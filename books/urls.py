from django.urls import path
from views import BookListView, BookAddView, BookDeleteView


urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('add/', BookAddView.as_view(), name='add'),
    path('delete/', BookDeleteView.as_view(), name='delete'),

]
