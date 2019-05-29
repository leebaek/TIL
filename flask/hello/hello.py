from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/mulcam')
def mulcam():
    return 'This is Multicampus!'

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다, {name}님!'

@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return f'{result}' # f스트링의 결과는 항상 문자다.


# 사람 수 만큼 점심메뉴 추천하기
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['피자', '치킨', '햄버거', '짜장면', '냉면', '김밥', '스시']
    return f'{random.sample(menu, people)}' # 뽑힌 내용이 list라서 string으로 변경해줘야 함.


@app.route('/html')
def html():
    multiple_string = """
        <h1>This is h1 tag!</h1>
        <p>This is p tag!</p>
    """
    return multiple_string


@app.route('/html_file')
def html_file():
    return render_template('html_file.html')


# template variable(변수)
@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', your_name=name)


@app.route('/menu_list')
def menu_list():
    menu = ['피자', '치킨', '햄버거', '짜장면', '냉면', '김밥', '스시', '롤']
    return render_template('menu_list.html', menu_list=menu)


if __name__ == '__main__':
    app.run(debug=True)