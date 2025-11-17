from django.shortcuts import render

def editorial_views(request):
    return render(request, 'editorial/editorial.html')