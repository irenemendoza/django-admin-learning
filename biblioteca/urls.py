from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from debug_toolbar.toolbar import debug_toolbar_urls
from .views import home_view, contact_view, search_view, SetLanguageView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("i18n/", include('django.conf.urls.i18n')),
    path('accounts/', include('django.contrib.auth.urls')),
] + debug_toolbar_urls()

urlpatterns += i18n_patterns(
    path("buscar/", search_view, name = "search"),
    path("", home_view, name = "home"),
    path('editorial/', include('books.urls.editoriales_urls', namespace="editorial")),
    path('libro/', include('books.urls.libros_urls', namespace="libro")),
    path('autor/', include('books.urls.autores_urls', namespace="autor")),
    
    path('admin/', admin.site.urls),
    path('contact', contact_view, name = "contacto"),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls')),
    ]