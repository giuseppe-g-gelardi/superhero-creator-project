from django.shortcuts import render
from django.http import HttpResponse
from .models import Superheroes
# Create your views here.


def index(request):
    all_superheroes = Superheroes.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'myapp/index.html', context)

def detail(request, superhero_id):
    superhero_id = Superheroes.objects.get(pk=superhero_id)

    return render(request, 'myapp/index.html')