import requests

key = "정해야 되욤~"
city = "Gumi"
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

response = requests.get(url).json()

print(response)
