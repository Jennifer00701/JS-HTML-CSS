import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_user = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url = input("검색어를 입력해주세요")

url = base_user + search_url
req =requests.get(url, headers = header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

areas = soup.select(".view_wrap")

for i in areas :
    ad = i.select_one(".link_ad")
    if ad :
        continue # 출력 안 하고 넘어가게 
        # print("광고다")  출력
    else:
        title = i.select_one(".title_link._cross_trigger")
        name = i.select_one(".user_info")
        print(f" 글 제목 : {title.text}")
        print(f" 글 작성자 : {name.text}")
        print(f" 글 링크 : {title['href']}")
        print() 