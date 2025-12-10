from django.urls import path
from books.views import (
AutorListView, 
AutorDetailView, 
AutorCreateView,
AutorUpdateView,
AutorDeleteView
)

app_name = "autor"

urlpatterns = [
    path('autor/lista/', AutorListView.as_view(), name="list"),
    path('autor/create/', AutorCreateView.as_view(), name="create"),
    path('autor/<pk>/', AutorDetailView.as_view(), name="detail"),
    path('autor/update/<pk>', AutorUpdateView.as_view(), name="update"),
    path('autor/delete/<pk>', AutorDeleteView.as_view(), name="delete"),
    ]