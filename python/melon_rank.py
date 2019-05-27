import requests
import bs4

# 406에러가 떴을 때 headers를 지정해준다 : 개발자도구 -> Network탭 -> headers탭 -> User-Agent....복붙
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

response = requests.get('https://www.melon.com/chart/index.htm', headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')
songs = soup.select('#lst50')

with open('melon_rank.csv', 'w', encoding='utf-8') as f:
    for song in songs:
        rank = song.select_one('td:nth-child(2) > div > span.rank').text
        title = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
        artist = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
        f.write(f'{rank}위, {title}, {artist}\n')