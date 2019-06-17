from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm
from IPython import embed

def index(request):
    # boards = Board.objects.order_by('-id')
    boards = Board.objects.all()[::-1]
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)


def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        # embed()
        if form.is_valid(): # form의 유효성검사
            title = form.cleaned_data.get('title') # 정제를 해준다.
            content = form.cleaned_data.get('content')
            board = Board.objects.create(title=title, content=content) # 세번째 방법, 저장이 필요없다.
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {'form':form}
    return render(request, 'boards/create.html', context)


def detail(request, board_pk):
    # board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk)
    # board_pk에 해당하는 글이 있으면 띄우고 아니면 404에러를 띠워
    context = {'board':board}
    return render(request, 'boards/detail.html', context)


def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    return redirect('boards:detail', board.pk)


def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board.title = form.cleaned_data.get('title')
            board.content = form.cleaned_data.get('content')
            board.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm(initial=board.__dict__)
        # 초기값 / 이걸 해줘야 글 작성한 내용을 볼 수 있음.
    context = {'form':form}
    return render(request, 'boards/create.html', context)
    # form이라는 인스턴스 객체를 만들어서 초기값을 설정해주었기 때문에 create.html인데도 수정이 가능함.