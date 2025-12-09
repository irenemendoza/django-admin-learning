from django.urls import path
from books.views import 
LibroListView, 
LibroDetailView, 
LibroCreateView, 
LibroUpdateView, 
LibroDeleteView


app_name = "books"

urlpatterns = [
    path('libro/', LibroListView.as_view(), name="libro_list"),
    path('libro/detail/<pk>', LibroDetailView.as_view(), name="libro_detail"),
    path('libro/createbook', LibroCreateView.as_view(), name="libro_create"),
    path('libro/updatebook/<pk>', LibroUpdateView.as_view(), name="libro_update"),
    path('libro/deletebook/<pk>', LibroDeleteView.as_view(), name="libro_delete"),
]
