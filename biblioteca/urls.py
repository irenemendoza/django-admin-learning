from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from .views import home_view, contact_view, search_view


urlpatterns = [
    path("", home_view, name = "home"),
    path("books/", include('books.urls', namespace="books")),
    path("buscar/", search_view, name = "search"),
    path('admin/', admin.site.urls),
    path('contact', contact_view, name = "contacto"),
] + debug_toolbar_urls()
