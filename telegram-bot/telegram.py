import requests
import random
from decouple import config

# telegram token
token = config('TELE_TOKEN')

# telegram api
api_url = f'https://api.telegram.org/bot{token}'

# 본인 telegram 계정 id
chat_id = config('CHAT_ID')

# text = input('메세지를 입력하세요: ')
text = random.sample(range(1, 46), 6)

response = requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')