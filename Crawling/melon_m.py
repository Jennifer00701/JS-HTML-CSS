from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


#옵션 설정
options = Options()
user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"
options.add_argument("user-agent=" + user )


options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)

#크롤링 코드 작성
url = "https://m2.melon.com/index.htm"
driver.get(url)

# url_c = driver.current_url
# 접속해져있는 url 출력 (main 이벤트 페이지나오는데 if 써서 기존 url 이랑 같지 않으면 (!=) 위 원래 url 출력 )
time.sleep(1)
if driver.current_url != url:
    driver.get(url)

time.sleep(0.5)
driver.find_element(By.LINK_TEXT, "닫기").click()
time.sleep(0.5)
driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(0.5)
more_Btn = driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
items = soup.select("#_chartList") 
list_items = list(items)
print(len(list_items))

num = 1
for i in items:
    title = i.select_one(".title.ellipsis")
    name = i.select_one(".name.ellipsis")
    print(f"순위 : [{num}]")
    print(f"노래 제목 : {title.text.strip()}")
    print(f"가수 이름 : {name.text.strip()}")
    print()
        
    num += 1



# 제목 가수 소개 가져오기 .
    #/ 월기준 상승한 클레스, 다운 거르기 - 상승한 순위 - 과제 / 어제 
# id 가 똑같을 때 (find_element는 하나 elements 는 여러개 뽑을 수 있음)
# more_Btn = driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()
# 버튼이라 바로 누를 수 있다. 인덱싱 상에서 1번(2번) 을 클릭하도록 []리스트형태