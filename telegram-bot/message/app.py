from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route('/write')
def write():
    return render_template('write.html')


@app.route('/send')
def send():
    token = '881065264:AAHaTrftk2i6M3eo_ED9z00iYBTbME5Inn4'
    api_url = f'https://api.telegram.org/bot{token}'
    chat_id = '846753598'
    # text = input('메세지를 입력하세요: ')
    # text = random.sample(range(1, 46), 6)
    text = request.args.get('message')

    response = requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')
    return '전송 완료!'


if __name__ == '__main__':
    app.run(debug=True)