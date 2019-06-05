from django.shortcuts import render
from .models import Board # 같은 경로에 있는 models.py에서 Board 클래스를 import

def index(request):
    return render(request, 'boards/index.html')

def new(request):
    return render(request, 'boards/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    board = Board(title=title, content=content) # column들의 이름 : 변수
    board.save() # DB에 저장

    return render(request, 'boards/create.html')