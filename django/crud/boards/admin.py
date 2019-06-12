from django.contrib import admin
from .models import Board # Board 클래스를 불러옴

# 각 column으로 정리해서 보여주기
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at', )

admin.site.register(Board, BoardAdmin) # Board, BoardAdmin 클래스를 등록
