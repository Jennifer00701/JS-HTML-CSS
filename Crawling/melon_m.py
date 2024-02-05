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

url_c = driver.current_url
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
time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
items = soup.select(".service_list.list_music>.list_item") 
# .service_list .list_music의 클래스 명을 가지고 있는 태그의
# 자식에 .list_item을 가지고 오겠다

# print(items)
# list_items = list(items)
# print(len(list_items))

num = 1
for i in items:
    title = i.select_one(".title.ellipsis")
    name = i.select_one(".name.ellipsis")
    print(f"순위 : [{num}]")
    print(f"노래 제목 : {title.text.strip()}")
    print(f"가수 이름 : {name.text.strip()}")
    print()

    num += 1

driver.find_element(By.LINK_TEXT, "홈").click()
time.sleep(1)

n1 = soup.select(".swiper_slide.main_home>.service_list.list_album.grid_type>.list_item")

number = 1
print("<------최신 음악 리스트 입니다.----->")
print("이곳은 멜론 페이지에 의하여 실시간으로 변동됩니다.")
print()
for i in n1 :
    home = i.select_one(".title.ellipsis.line_clamp2")
    sing = i.select_one(".name.ellipsis")
    lef = i.select_one(".left.top")
    print([number])
    print(f" 제목 : {home.text}")
    print(f" 가수: {sing.text}")
    print(f" Update : {lef.text} ")
    print()
    number += 1

    print("자세히 보기 : https://m2.melon.com/index.htm ")
    print()
driver.find_element(By.LINK_TEXT, "티켓").click()
time.sleep(1)

n2 = soup.select(".ticket.hit > ul > li")

numm = 1
print("<----24년 놓치지 말아야 할 공연 리스트입니다.---->")
print()
for i in n2:
    place = i.select_one(".date")
    Music = i.select_one(".subject.ellipsis")
    print([numm])
    print(f"공연 이름은 : {Music}")
    # print(f"공연 날짜는 : {ddy}")
    print(f"공연 장소는 : {place}")

    numm += 1



driver.find_element(By.LINK_TEXT, "콘서트 랭킹").click()
time.sleep(1)

print("<----콘서트/패스티벌 랭킹 순위 입니다.---->")
time.sleep(1)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# 이 부분이 핵심 콘서트 패스티벌 랭킹 순위로 이동 하였지만 
# 그 부분에서의 html/css/js 코드는이전과는 분명 다름 
# 그렇기 때문에 다시 한번 코드를 받아와서파싱을 진행해야 
# 그 위치에서 찾고자 하는 클래스, 아이디, 태그 등등을 찾을 수 있음

time.sleep(1)
festi = soup.select(".list_ranking, .inner")
time.sleep(1)

for i in festi:
    title = i.select_one(".tit")
    print(f" 제목 : {title.text}")


# 제목 가수 소개 가져오기 .
    #/ 월기준 상승한 클레스, 다운 거르기 - 상승한 순위 - 과제 / 어제 
# id 가 똑같을 때 (find_element는 하나 elements 는 여러개 뽑을 수 있음)
# more_Btn = driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()
# 버튼이라 바로 누를 수 있다. 인덱싱 상에서 1번(2번) 을 클릭하도록 []리스트형태