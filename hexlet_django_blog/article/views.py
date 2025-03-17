from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = 'articles'
    return render(
        request,
        'articles/index.html',
        context={'name': name},
    )

# Create your views here.
