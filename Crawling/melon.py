import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "https://www.melon.com/chart/index.htm"
req =requests.get(url, headers = header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

lst50 = soup.select(".lst50")
# .lst 50에 해당 클레스 모든 것 추출
lst100 = soup.select(".lst100") 

# lst_all = lst50 + lst100
lst_all = soup.find_all(class_=["lst50","lst100"])

num = 1 
# enumerate # 자동으로 숫자를 만들어주는 내장 함수 
# for lank, i in enumerate(lst_all,1): 
# 0부터 시작이라 1입력
for i in lst_all:
    tltle = i.select_one(".ellipsis.rank01 a")
    singer = i.select_one(".ellipsis.rank02 a")
    album = i.select_one(".ellipsis.rank03 a")


    print(f"[순위]{num}")
    print(f"제목 : {tltle.text}")
    print(f"가수 : {singer.text}")
    print(f"앨범:{album.text}")
    print()
    num +=1
