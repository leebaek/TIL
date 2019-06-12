from django.shortcuts import render, redirect
from .models import Board, Comment # 같은 경로에 있는 models.py에서 Board 클래스를 import

def index(request):
    # boards = Board.objects.order_by('-id') # django ORM으로 내림차순 정렬
    boards = Board.objects.all()[::-1] # python으로 내림차순 정렬
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        board = Board(title=title, content=content)  # column들의 이름 : 변수
        board.save()  # DB에 저장

        # return render(request, 'boards/create.html') # 글을 작성하고 제출하면 '작성완료'창으로 이동
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/new.html')


def detail(request, board_pk): # 글을 작성하면 그 글로
    board = Board.objects.get(pk=board_pk)
    comments = board.comment_set.all()
    context = {'board':board, 'comments':comments}
    return render(request, 'boards/detail.html', context)

def delete(request, board_pk): # variable routing? 특정값을 변수화하여 인자로 넘기기 위해(pk)
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)


def edit(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        context = {'board':board}
        return render(request, 'boards/edit.html', context)


def comments_create(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        comment = Comment()
        comment.board_id = board.pk
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('boards:detail', board.pk)
    else:
        return redirect('boards:detail', board.pk)

def comments_edit(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('boards:detail', board_pk)
    else:
        context = {'comment':comment}
        return render(request, 'boards/comments_edit.html', context)


def comments_delete(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('boards:detail', board_pk)
    else:
        return redirect('boards:detail', board_pk)