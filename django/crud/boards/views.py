from django.shortcuts import render, redirect
from .models import Board # 같은 경로에 있는 models.py에서 Board 클래스를 import

def index(request):
    # boards = Board.objects.order_by('-id') # django ORM으로 내림차순 정렬
    boards = Board.objects.all()[::-1] # python으로 내림차순 정렬
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)

def new(request):
    return render(request, 'boards/create.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    board = Board(title=title, content=content) # column들의 이름 : 변수
    board.save() # DB에 저장

    # return render(request, 'boards/create.html') # 글을 작성하고 제출하면 '작성완료'창으로 이동
    return redirect(f'/boards/{board.pk}/') # 글을 작성하고 제출하면 글을 확인하는 창으로 이동

def detail(request, pk): # 글을 작성하면 그 글로
    board = Board.objects.get(pk=pk)
    context = {'board':board}
    return render(request, 'boards/detail.html', context)

def delete(request, pk): # variable routing? 특정값을 변수화하여 인자로 넘기기 위해(pk)
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('/boards/')

def edit(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board':board}
    return render(request, 'boards/edit.html', context)

def update(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect(f'/boards/{board.pk}/')