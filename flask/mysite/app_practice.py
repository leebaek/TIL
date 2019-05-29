from flask import Flask, render_template, request
import random
app = Flask(__name__)

# send 페이지에서 입력 후 제출하여 receive 페이지로 값을 넘겨준다.

@app.route('/send_practice')
def send():
    return render_template('send_practice.html')


@app.route('/receive_practice')
def receive():
    # dictionary형태로 send 페이지에서 입력한 내용을 받는다.
    # {user : 'wow', message : 'wow'}
    #user = request.args.get('user') # => baekjin
    happyage = random.randrange(35,55)
    return render_template('receive_practice.html', user=happyage)

if __name__ == '__main__':
    app.run(debug=True)