from django.urls import path
from catalog import views

#app_name = "catalog"
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<uuid:pk>', views.BookDetailView.as_view(), name='book-detail'),
]