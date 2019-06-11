from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'), # name='별명'
    path('new/', views.new, name='new'),
    path('<int:board_pk>/', views.detail, name='detail'), # 정수의 pk라는 변수에 담겠다.
    path('<int:board_pk>/delete/', views.delete, name='delete'),
    path('<int:board_pk>/edit/', views.edit, name='edit'),
    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
]

