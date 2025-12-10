from django.urls import path
from books.views import (
LibroListView, 
LibroDetailView, 
LibroCreateView, 
LibroUpdateView, 
LibroDeleteView
)

app_name = "libro"

urlpatterns = [
    path('libro/', LibroListView.as_view(), name="list"),
    path('libro/createbook', LibroCreateView.as_view(), name="create"),
    path('libro/detail/<pk>', LibroDetailView.as_view(), name="detail"),
    path('libro/updatebook/<pk>', LibroUpdateView.as_view(), name="update"),
    path('libro/deletebook/<pk>', LibroDeleteView.as_view(), name="delete"),
]
