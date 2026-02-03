import requests
from pprint import pprint


# citysame = "Seoul,KR"
# 서울 위/경도
lat = 37.56
lon = 126.97
apikey = 'b59c9d0f5650af66afedeaf69c0b2dfb'


url = f"https://api.openweathermap.org/data/2.5/weather?lat={}&lon=100&appid=[apikey]"

response = requests.get(url).json()
pprint(response)

https://api.openweathermap.org/data/2.5/weather?lat=35&lon=100&appid=b59c9d0f5650af66afedeaf69c0b2dfb