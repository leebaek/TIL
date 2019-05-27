# pip install requests
import requests
import bs4
import datetime

html = requests.get('https://www.naver.com').text
soup = bs4.BeautifulSoup(html, 'html.parser')

ranks = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k') # class 따오기
now = datetime.datetime.now()

with open('naver_rank.txt', 'w', encoding='utf-8') as f:
    f.write(f'{now} 현재 기준 네이버 검색어 순위입니다.\n')

    # enumerate : for문에서 index를 함께 지정할 때, ranks는 rank에 index는 i에 저장
    for i, rank in enumerate(ranks):
        f.write(f'{i+1}. {rank.text}\n')