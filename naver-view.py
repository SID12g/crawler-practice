import requests
from bs4 import BeautifulSoup

data = requests.get('https://s.search.naver.com/p/review/search.naver?rev=43&where=view&api_type=11&start=61&query=%EC%82%AC%EA%B3%BC')

soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser')

list = soup.select('a.title_link')

print(list[0]['href'])
print(list[1].text)
print(list[2].text)