import requests
from bs4 import BeautifulSoup

def price(code):
    data = requests.get('https://finance.naver.com/item/sise.naver?code='+code)
    soup = BeautifulSoup(data.content, 'html.parser')
    return soup.select('strong#_nowVal')[0].text

print('samsung: ',price('005930'))
print('lg: ',price('003555'))

list = ['005930', '066575', '005380', '035720', '034220', '003490']

File = open('a.csv', 'w')
File.write(price(list[0])+'\n')
File.write(price(list[1])+'\n')
File.write(price(list[2])+'\n')
File.write(price(list[3])+'\n')
File.write(price(list[4])+'\n')
File.write(price(list[5]))
File.close()

# data = requests.get('https://finance.naver.com/item/main.naver?code=005930')
# soup = BeautifulSoup(data.content, 'html.parser')

# dd = soup.find_all('em', class_="no_down")[0].text
# dd2 = soup.find_all('td', class_="f_down")[0].text
# dd3 = soup.select('td.f_down em')[0].text
# imge = soup.select('img#img_chart_area')[0]
# print(imge['src'])

# link = requests.get('https://finance.naver.com/item/main.naver?code=003555')
# soup = BeautifulSoup(link.content, 'html.parser')
# dd = soup.find_all('em', class_="no_up")[0].text
# print(dd)

