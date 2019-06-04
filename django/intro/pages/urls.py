from django.urls import path
from . import views # views.py와 동일한 위치에 있기 때문에 .에서 views를 쓰겠다!

urlpatterns = [
    path('index/', views.index),
    path('hola/', views.hola), # view.py의 hola함수~
    path('dinner/', views.dinner),
    # <> 사용자가 입력하는 내용
    path('hello/<str:name>/', views.hello), # str:name => default가 str이기 때문에 생략가능.
    path('introduce/<name>/<int:age>/', views.introduce),
    path('mul/<int:first>/<int:second>/', views.mul),
    path('area/<int:r>/', views.area),
    path('template_language/', views.template_language),
    path('birthday/', views.birthday),
    path('isbirth/', views.isbirth),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('lotto/', views.lotto),
    path('number/', views.number),
    path('lotto2/', views.lotto2),
    path('picklotto/', views.picklotto),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]
