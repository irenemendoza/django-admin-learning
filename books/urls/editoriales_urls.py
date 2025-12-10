from django.urls import path
from books.views import (
EditorialListView, 
EditorialCreateView, 
EditorialDetailView, 
EditorialUpdateView, 
EditorialDeleteView
)

app_name = "editorial"

urlpatterns = [
    path('editorial/lista/', EditorialListView.as_view(), name="list"),
    path('editorial/create/', EditorialCreateView.as_view(), name="create"),
    path('editorial/<pk>/', EditorialDetailView.as_view(), name="detail"),
    path('editorial/update/<pk>', EditorialUpdateView.as_view(), name="update"),
    path('editorial/delete/<pk>', EditorialDeleteView.as_view(), name="delete"),
    ] 
