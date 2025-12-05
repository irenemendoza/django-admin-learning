from django.urls import path
from .views.autor_views import autor_views, autor_detail
from .views.libro_views import libro_views
from .views.editorial_views import editorial_views, editorial_create_views


app_name = "books"

urlpatterns = [
    path('autor/', autor_views, name="autor_list"),
    path('autor/<int:id>/', autor_detail, name="autor_detail"),
    path('editorial/', editorial_views, name="editorial_list"),
    path('libro/', libro_views, name="libro_list"),
    path('editorial/create/', editorial_create_views, name="editorial_create")
] 
