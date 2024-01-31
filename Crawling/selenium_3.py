from selenium import webdriver
from bs4 import BeautifulSoup
import time

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_user = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url = input("검색어를 입력해주세요")

url = base_user + search_url
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

# 스크롤 코드
# driver.execute_script("window.scrollTo(0,4000)")

# 스크롤 끝까지 내리기
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(6)

for i in range(5):
    #  0부터 4까지의 숫자를 생성하는 범위(range)를 나타냄
    # 즉, 0, 1, 2, 3, 4의 값을 순차적으로 i에 할당하면서 반복 작업이 수행됨
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)

html = driver.page_source # html = req.text
soup = BeautifulSoup(html, "html.parser")
areas = soup.select(".view_wrap")

num = 1
for i in areas:
    ad = i.select_one(".link_ad")
    if ad :
        continue
    else :
        title = i.select_one(".title_link._cross_trigger") 
        name = i.select_one(".user_info > a")
        print(num)
        print (f"글 제목 : {title.text}")
        print (f"글 작성자 : {name.text}")
        print (f"글 링크 : {title['href']}")

        print()

        num +=1