from django.urls import path
from books.views import 
AutorListView, 
AutorDetailView, 
AutorCreateView,
AutorUpdateView,
AutorDeleteView

app_name = "books"

urlpatterns = [
    path('autor/lista/', AutorListView.as_view(), name="autor_list"),
    path('autor/ccbv/<pk>/', AutorDetail.as_view(), name="autor_detail"),
    path('autor/create/', AutorCreateView.as_view(), name="autor_create"),
    path('autor/update/', AutorUpdateView.as_view(), name="autor_update"),
    path('autor/delete/', AutorDeleteView.as_view(), name="autor_delete"),
    ]