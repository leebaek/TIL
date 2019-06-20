from django.db import models
from django.conf import settings


class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_boards', blank=True)
    # AUTH_USER_MODEL : 장고가 기본적으로 갖고 있는 유저 모델
    # blank=True : 값이 없을 수도 있기 때문에(좋아요가 눌리지 않을 수 있기 때문에 설정해줌.)
    # on_delete=models.CASCADE : 회원탈퇴를 하면 작성된 게시글이 함께 삭제 됨.
    def __str__(self):
        return f'글 번호{self.id}, 글 제목 -> {self.title}, 글 내용 -> {self.content}'


# 사용자와 댓글의 관계를 1:N으로 만들어줌.
class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    # class Meta:
    #     ordering = ('-pk',) # ,를 찍어야 튜플이 됨.
        # 최신 댓글이 상단에 위치하도록 함.