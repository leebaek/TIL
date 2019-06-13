from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

def board_image_path(instance, filename):
    return f'boards/{instance.pk}번글/images/{filename}'

class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to=board_image_path,
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality':90}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    content = models.CharField(max_length=200) # 댓글의 내용
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE) # 댓글에 해당하는 게시글을 나타낸다.

    def __str__(self):
        return f'<Board{self.board_id}: Comment({self.id} - {self.content})>'

    # 생성 후
    # $ python manage.py makemigrations
    # $ python manage.py migrate