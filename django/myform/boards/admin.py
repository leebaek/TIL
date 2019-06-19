from django.contrib import admin
from .models import Board, Comment

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at')

admin.site.register(Board, BoardAdmin) # admin페이지에서 볼 수 있게


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content',)

admin.site.register(Comment, CommentAdmin)