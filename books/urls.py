from django.urls import path
from .views import (autor_views, libro_views, editorial_views)


urlpatterns = [
    path('autor', autor_views),
    path('editorial', editorial_views),
    path('libro', libro_views),
] 
