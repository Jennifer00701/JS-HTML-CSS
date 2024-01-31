import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_user = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url = input("검색어를 입력해주세요")

url = base_user + search_url
req =requests.get(url, headers = header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

soup.find(class_="link_service", text = '뉴스')
soup.find(id = "link_service")
# find = select_one
# find_all = select  
# select -> . # 사용했다면 find 는 id = "" 사용, class_= "" 적어야함