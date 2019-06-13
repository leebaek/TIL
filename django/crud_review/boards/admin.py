from django.contrib import admin
from .models import Board, Comment # Board 클래스를 불러옴

# 각 column으로 정리해서 보여주기
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'image', 'created_at', 'updated_at', )

admin.site.register(Board, BoardAdmin) # Board, BoardAdmin 클래스를 등록


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'updated_at', )

admin.site.register(Comment, CommentAdmin)