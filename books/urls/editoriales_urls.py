from django.urls import path
from books.views import 
EditorialListView, 
EditorialCreateView, 
EditorialDetailView, 
EditorialUpdateView, 
EditorialDeleteView


app_name = "books"

urlpatterns = [
    path('editorial/lista/', EditorialListView.as_view(), name="editorial_list"),
    path('editorial/ccbv/<pk>/', EditorialDetail.as_view(), name="editorial_detail"),
    path('editorial/create/', EditorialCreateView.as_view(), name="editorial_create"),
    path('editorial/update/', EditorialUpdateView.as_view(), name="editorial_update"),
    path('editorial/delete/', EditorialDeleteView.as_view(), name="editorial_delete"),
    ] 
