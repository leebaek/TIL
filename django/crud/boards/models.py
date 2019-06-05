from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=10) # 입력할 수 있는 글자의 수를 10으로 제한.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 처음 생성할 때의 시간.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): # 매직매서드 : 특별한 목적이 있다.
        return f'{self.id}번글 - {self.title} : {self.content}'
        # board.id, board.title, board.content와 같은 의미