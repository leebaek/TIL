from django.shortcuts import render

def index(request):
    return render(request, 'utilities/index.html')

def lorem(request):
    return render(request, 'utilities/lorem.html')