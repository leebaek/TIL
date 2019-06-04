from django.shortcuts import render
import random
from datetime import datetime
import json
import requests

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def hola(request):
    return render(request, 'pages/hola.html')

def dinner(request):
    menu = ['자장면', '치킨', '버거킹', '삼겹살', '갈비', '냉면', '만두', '탕수육']
    pick = random.choice(menu)
    context = {'pick':pick} # dinner.html에서 설정한 이름 {{ pick }} : pick변수
    return render(request, 'pages/dinner.html', context)

def hello(request, name): # 함수를 정의할 때, name인자를 미리 설정해줄 수 있다.
    context = {'name':name}
    return render(request, 'pages/hello.html', context)

def introduce(request, name, age):
    context = {'name':name, 'age':age}
    return render(request, 'pages/introduce.html', context)

# variable routing을 통해 숫자 2개를 받아 곱셈 결과를 출력
def mul(request, first, second):
    multiply = first * second
    context = {'first':first, 'second':second, 'multiply':multiply}
    return render(request, 'pages/mul.html', context)

# 반지름(r)을 인자로 받아 원의 넓이를 출력
def area(request, r):
    result = r ** 2 * 3.14
    context = {'r':r, 'result':result}
    return render(request, 'pages/area.html', context) # 세번째 인자는 반드시 딕셔너리여야 한다.

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
    return render(request, 'pages/template_language.html', context)

# is it my birthday?_1
def birthday(request):
    today = datetime.now()
    month = today.month
    day = today.day
    context = {'month':month, 'day':day}
    return render(request, 'pages/birthday.html', context)

# is it my birthday?_2
def isbirth(request):
    today = datetime.now()
    if today.month == 2 and today.day == 5:
        result = True
    else:
        result = False
    context = {'result':result}
    return render(request, 'pages/isbirth.html', context)

# 던지고 받는 흐름 이해
def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {'message':message, 'message2':message2}
    return render(request, 'pages/catch.html', context)

# lotto / number
# number -> 1~45의 수 중에서 6개를 뽑아 리스트로 만들어 넘긴다.
# number -> 사용자로부터 이름을 입력받아 넘긴다.
def lotto(request):
    return render(request, 'pages/lotto.html')

def number(request):
    list = range(1, 46)
    number = random.sample(list, 6)
    name = request.GET.get('name') # lotto.html에서 보낸 name을 받아서 넘긴다.
    context = {'number':number, 'name':name} # {받는 html에서 사용할 이름:위에서 정의한 변수}
    return render(request, 'pages/number.html', context)

def lotto2(request):
    return render(request, 'pages/lotto2.html')

def picklotto(request):
    name = request.GET.get('name')

    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=861')
    lotto = json.loads(res.text) # 응답받은 결과를 딕셔너리 형태로 바꿔주기 위해 json모듈을 사용!

    winner = []
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}']) # 대괄호를 사용하여 value를 구하기 위함.
    picked = sorted(random.sample(range(1, 46), 6))
    matched = len(set(winner) & set(picked)) # list는 &연산자를 쓰지 못하기 때문에 set으로 감싸준다.

    if matched == 6:
        result = '1등입니다. 퇴사!'
    elif matched == 5:
        result = '3등입니다. 휴가 ㄱㄱ!'
    elif matched == 4:
        result = '4등입니다. 그냥 놀아..'
    elif matched == 3:
        result = '5등입니다. 그거로 로또사'
    else:
        result = '꽝입니다. 대표님 충성충성'

    context = {'name':name, 'result':result}
    return render(request, 'pages/picklotto.html', context)


def art(request):
    return render(request, 'pages/art.html')

def result(request):
    #1. form 태그로 날린 데이터를 받는다.
    word = request.GET.get('word')

    #2. artii API를 통해 보낸 응답 결과를 text로 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    #3. fonts(str)를 font 리스트의 형태로 저장한다.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서 font에 저장한다.
    font = random.choice(fonts)

    #5. 위에서 사용자에게 받은 word와 랜덤으로 뽑은 font를 가지고 다시 요청을 보낸다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {'result':result}
    return render(request, 'pages/result.html', context)

def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name':name, 'pwd':pwd}
    return render(request, 'pages/user_create.html', context)

def static_example(request):
    return render(request, 'pages/static_example.html')