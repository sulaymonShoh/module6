from django.shortcuts import render
from .models import Todo


# Create your views here.
def home_page(request):
    return render(request, 'todo/home.html', context={"tfodos": Todo.objects.all()})
