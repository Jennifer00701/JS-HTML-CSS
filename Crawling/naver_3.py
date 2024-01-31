import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
serch_url = input("검색어를 입력해주세요 : ")
base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="

url = base_url+serch_url
req =requests.get(url, headers = header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")


keyword_box = soup.select(".keyword_box_wrap.type_color")
title = soup.select(".news_tit")

n = 1
for i in title :
    title = i.text
    # 뉴스 tit 클래스 가져온 것 
    print(f"{n}번 돌았다.")
    print(f"손흥민 뉴스 제목은 : {title}")
    print(f"뉴스 링크 : {i['href']}")
    print()

    n +=1
# i.text -> 태그 밖 -> 텍스트 출력 가능 



# title = soup.select(".link_tit")
# 개발자 도구에서 타이틀 클라스 가져온 것

# for i in title :
#     print(i. text)
#     print (i['href'])
#     print()

