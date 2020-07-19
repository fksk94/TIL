import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"

response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')

select = data.select_one("#KOSPI_now")
print(select.text)
