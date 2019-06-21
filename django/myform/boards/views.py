from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Board, Comment
from .forms import BoardForm, CommentForm
from IPython import embed


def index(request):
    # boards = Board.objects.order_by('-id')
    boards = Board.objects.all()[::-1] # 최신글을 상단으로 모든 게시글을 띄운다.
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)

@login_required # 로그인 없이는 글작성을 하지 못하게 함.
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST) # form에 BoardForm틀로 POST요청으로 받은 내용을 담는다
        # embed()
        if form.is_valid(): # form의 유효성검사(True or False)
            # title = form.cleaned_data.get('title') # 딕셔너리형에서 .get('title')의 내용을 추출
            # content = form.cleaned_data.get('content')
            # board = Board.objects.create(title=title, content=content) # 세번째 방법, 저장이 필요없다.
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm() # form.html의 폼으로(빈 폼)
    context = {'form':form}
    return render(request, 'boards/form.html', context)


def detail(request, board_pk):
    # board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk)
    # board_pk에 해당하는 글이 있으면 띄우고 아니면 404에러를 띄워
    person = get_object_or_404(get_user_model(), pk=board.user.pk)
    comments = board.comment_set.all() # 게시판에 달린 모든 글을 가져옴.
    comment_form = CommentForm() # 댓글 적는 곳
    context = {'board':board, 'comments':comments, 'comment_form':comment_form, 'person':person}
    return render(request, 'boards/detail.html', context)


def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user: # board.user : 게시글을 작성한 유저, request.user : 로그인한 사용자
        if request.method == 'POST':
            board.delete()
            return redirect('boards:index')
        else:
            return redirect('boards:detail', board.pk)
    else:
        return redirect('boards:index')


@login_required # 로그인 없이는 글수정을 하지 못하게 함.
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk) # 기존 글을 가져옴.
    if board.user == request.user:
    # board.user : 게시글을 작성한 유저, request.user : 로그인한 사용자/같으면 수정가능, 다르면 index로
        if request.method == 'POST':
            form = BoardForm(request.POST, instance=board)
            if form.is_valid():
                # board.title = form.cleaned_data.get('title')
                # board.content = form.cleaned_data.get('content')
                # board.save()
                form.save()
                return redirect('boards:detail', board.pk)
        else:
            form = BoardForm(instance=board)
            # 초기값 / 이걸 해줘야 글 작성한 내용을 볼 수 있음.
    else:
        return redirect('boards:index')
    context = {'form': form, 'board': board}
    return render(request, 'boards/form.html', context)
    # form이라는 인스턴스 객체를 만들어서 초기값을 설정해주었기 때문에 create.html인데도 수정이 가능함.


@login_required
@require_POST # POST요청을 제외한 요청에는 405에러를 띄운다.
def comments_create(request, board_pk):
    comments_form = CommentForm(request.POST)
    if comments_form.is_valid():
        comment = comments_form.save(commit=False)
        comment.user = request.user
        comment.board_id = board_pk
        comment.save()
    return redirect('boards:detail', board_pk)


@login_required
@require_POST
def comments_delete(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.user: # 유저가 댓글을 쓴 유저와 다를 때, detail페이지로 / 아니면 댓글 삭제
        return redirect('boards:detail', board_pk)
    comment.delete()
    return redirect('boards:detail', board_pk)


@login_required
def like(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)

    if request.user in board.like_users.all():
    # 게시글에 좋아요를 누른 모든 유저 중에 어떤 유저가 있다면
        board.like_users.remove(request.user)
        # remove : 중개 테이블에 어떤 유저를 지워준다.(좋아요를 하나 누르면 또 다시 누르지 못하도록)
    else:
        board.like_users.add(request.user)
        # 조건에 맞지 않으면 중개 테이블에 어떤 유저를 넣어준다.
    return redirect('boards:index')


@login_required
def follow(request, board_pk, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user in person.followers.all():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    return redirect('boards:detail', board_pk)