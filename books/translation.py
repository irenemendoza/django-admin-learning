from modeltranslation.translator import translator, TranslationOptions
from .models import Autor, Editorial, Libro

class AutorTranslationOptions(TranslationOptions):
    fields = ('nacionalidad', 'biografia')

translator.register(Autor, AutorTranslationOptions)

class EditorialTranslationOptions(TranslationOptions):
    fields = ('nombre',)

translator.register(Editorial, EditorialTranslationOptions)

class LibroTranslationOptions(TranslationOptions):
    fields = ('titulo', 'descripcion')

translator.register(Libro, LibroTranslationOptions)