import requests
from pprint import pprint

url = "https://fakestoreapi.com/carts"

# API 요청 보내기
response = requests.get(url).json() #  response자체는 리스트타입임.
pprint(response) # 200이면정상 404면 오류