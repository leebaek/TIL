from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hola(request):
    return render(request, 'hola.html')

def dinner(request):
    menu = ['자장면', '치킨', '버거킹', '삼겹살', '갈비', '냉면', '만두', '탕수육']
    pick = random.choice(menu)
    context = {'pick':pick} # dinner.html에서 설정한 이름 {{ pick }} : pick변수
    return render(request, 'dinner.html', context)

def hello(request, name): # 함수를 정의할 때, name인자를 미리 설정해줄 수 있다.
    context = {'name':name}
    return render(request, 'hello.html', context)

def introduce(request, name, age):
    context = {'name':name, 'age':age}
    return render(request, 'introduce.html', context)

# variable routing을 통해 숫자 2개를 받아 곱셈 결과를 출력
def mul(request, first, second):
    multiply = first * second
    context = {'first':first, 'second':second, 'multiply':multiply}
    return render(request, 'mul.html', context)

# 반지름(r)을 인자로 받아 원의 넓이를 출력
def area(request, r):
    result = r ** 2 * 3.14
    context = {'r':r, 'result':result}
    return render(request, 'area.html', context) # 세번째 인자는 반드시 딕셔너리여야 한다.

def template_language(request):
    menus = ['자장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = ['justin', 'hwang']
    datetimenow = datetime.now()
    context = {
        'menus':menus,
        'my_sentence':my_sentence,
        'messages':messages,
        'empty_list':empty_list,
        'datetimenow':datetimenow
    }
    return render(request, 'template_language.html', context)

# is it my birthday?_1
def birthday(request):
    today = datetime.now()
    month = today.month
    day = today.day
    context = {'month':month, 'day':day}
    return render(request, 'birthday.html', context)

# is it my birthday?_2
def isbirth(request):
    today = datetime.now()
    if today.month == 2 and today.day == 5:
        result = True
    else:
        result = False
    context = {'result':result}
    return render(request, 'isbirth.html', context)

# 던지고 받는 흐름 이해
def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {'message':message, 'message2':message2}
    return render(request, 'catch.html', context)

# lotto / number
# number -> 1~45의 수 중에서 6개를 뽑아 리스트로 만들어 넘긴다.
# number -> 사용자로부터 이름을 입력받아 넘긴다.
def lotto(request):
    return render(request, 'lotto.html')

def number(request):
    list = range(1, 45)
    number = random.sample(list, 6)
    name = request.GET.get('name') # lotto.html에서 보낸 name을 받아서 넘긴다.
    context = {'number':number, 'name':name}
    return render(request, 'number.html', context)