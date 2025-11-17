from django.shortcuts import render

def libro_views(request):
    return render(request, 'libro/libro.html')