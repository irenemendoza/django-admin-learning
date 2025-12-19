from datetime import datetime
from books.models import Libro, Editorial, Autor

def get_current_year_context_processor(request):
    current_year = datetime.now().year
    return {
        'current_year': current_year,
        'user_logged': request.user
    }

def statistics_books(request):
    return {
        'n_books': Libro.objects.all().count(),
        'n_editorials': Editorial.objects.all().count(),
        'n_autors': Autor.objects.all().count(),
    }