import requests
from bs4 import BeautifulSoup
    
header_user = {"user.Agen" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
serch_url = input("검색어를 입력하시오")

url = base_url + serch_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

keyword_box = soup.select(".keyword_box_wrap.type_color")

for i in keyword_box:
    name = i.select_one (".name.elss")
    short = i.select_one (".hlt")
    print(f"블로그 이름은 : {name.text}")
    print(f"분야 : {short.text}")
    print()