from django import forms
from .models import Board, Comment

# 게시글의 폼을 설정
class BoardForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(attrs={
            'class':'title',
            'placeholder':'Enter the title',
        })
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
            'class':'content-type',
            'rows':5,
            'cols':50,
            'placeholder':'Enter the content',
        })
    )
    class Meta:
        model = Board
        fields = ['title', 'content']

# 댓글의 폼을 설정
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]


# class BoardForm(forms.Form):
#     title = forms.CharField(
#         max_length=20,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class':'title',
#                 'placeholder':'Enter the title'
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class':'content-type',
#                 'rows':5,
#                 'cols':50,
#                 'placeholder':'Enter the content'
#             }
#         )
#     )