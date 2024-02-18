import requests
from bs4 import BeautifulSoup

data = requests.get('https://finance.naver.com/item/main.naver?code=005930')
soup = BeautifulSoup(data.content, 'html.parser')

dd = soup.find_all('em', class_="no_down")[0].text
dd2 = soup.find_all('td', class_="f_down")[0].text
dd3 = soup.select('td.f_down em')[0].text
imge = soup.select('img#img_chart_area')[0]
print(imge['src'])

link = requests.get('https://finance.naver.com/item/main.naver?code=003555')
soup = BeautifulSoup(link.content, 'html.parser')
dd = soup.find_all('em', class_="no_up")[0].text
print(dd)