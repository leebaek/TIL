from django.urls import path
from . import views

app_name = 'bs'

urlpatterns = [
    path('', views.intro, name='intro'),
    path('new/', views.new, name='new'),
    path('map_1/', views.map_1, name='map_1'),
    path('map_2/', views.map_2, name='map_2'),
    path('<int:history_pk>/', views.detail, name='detail'),
    path('<int:history_pk>/calculate/', views.calculate, name='calculate'),
    path('<int:history_pk>/edit/', views.update, name='update'),
    path('<int:history_pk>/delete/', views.delete, name='delete'),
]