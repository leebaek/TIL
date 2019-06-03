from django.contrib import admin
from django.urls import path
from pages import views # pages에서 view를 쓰겠다.

urlpatterns = [
    path('admin/', admin.site.urls),
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
]
