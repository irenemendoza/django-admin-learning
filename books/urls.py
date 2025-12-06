from django.urls import path
from .views.autor_views import autor_views, autor_detail, autor_create_views
from .views.libro_views import libro_views
from .views.editorial_views import editorial_views, editorial_create_views, editorial_detail_views


app_name = "books"

urlpatterns = [
    path('autor/', autor_views, name="autor_list"),
    path('autor/<int:id>/', autor_detail, name="autor_detail"),
    path('editorial/', editorial_views, name="editorial_list"),
    path('editorial/<int:id>/', editorial_detail_views, name="editorial_detail"),
    path('libro/', libro_views, name="libro_list"),
    path('editorial/create/', editorial_create_views, name="editorial_create"),
    path('autor/create/', autor_create_views, name="autor_create")
] 
