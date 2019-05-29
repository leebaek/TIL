from flask import Flask, render_template, request
import requests
app = Flask(__name__)

# send 페이지에서 입력 후 제출하여 receive 페이지로 값을 넘겨준다.

@app.route('/send')
def send():
    return render_template('send.html')


@app.route('/receive')
def receive():
    # dictionary형태로 send 페이지에서 입력한 내용을 받는다.
    # {user : 'wow', message : 'wow'}
    user = request.args.get('user') # => baekjin
    message = request.args.get('message')  # => wow
    return render_template('receive.html', user=user, message=message)


@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')


@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    # response.text # => string으로 리턴
    lotto = response.json() # => dict로 리턴

    # winner = [] # list()
    # for n in range(1, 7):
    #     winner.append(lotto[f'drwtNo{n}'])

    # list comprehension
    a = [lotto[f'drwtNo{n}'] for n in range(1, 7)] # => [로또 번호 출력됨]
    b = lotto['bnusNo']

    winner = f'{a} + {b}'

    # my_numbers 가져오기, 입력된 값이 문자열이기 때문에 리스트로 만들어줘야 함.
    my_numbers = [int(n) for n in request.args.get('my_numbers').split()] # => [1,2,3,4,5,6]

    # 같은 숫자 개수 찾기, set()자료형
    matched = len(set(a) & set(my_numbers)) # => 1 (교집합을 구해서 그것의 length를 구함)
    # a => {4, 8, 16, 25, 44, 45}
    # my_numbers => {1, 2, 3, 4, 5, 6}

    # 같은 숫자의 갯수에 따른 등수
    if matched == 6:
        result = '1등입니다!!!!'
    elif matched == 5:
        if lotto['bnusNo'] in my_numbers:
            result = '2등입니다!!!'
        else:
            result = '3등입니다!!'
    elif matched == 4:
        result = '4등입니다!'
    elif matched == 3:
        result = '5등입니다.'
    else:
        result = '꽝입니다..'



    return render_template('lotto_result.html', lotto=winner, lotto_round=lotto_round, my_numbers=my_numbers, result=result)

if __name__ == '__main__':
    app.run(debug=True)