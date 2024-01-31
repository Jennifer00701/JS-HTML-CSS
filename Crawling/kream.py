from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium. webdriver.common.by import By
from selenium. webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

options = Options()
user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
options.add_argument(f"User-Agent={user}")

options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)

url = "https://kream.co.kr/"
driver.get(url)

driver.find_element(By.CSS_SELECTOR, ".btn_search").click()
# css 요소에 접근하는 방식 -> 버튼 태그 클릭 (마지막에 액션)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림") 
# ("슈프림\n") 도 엔터 기능 가능 
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)

for i in range(20) :
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    driver.save_screenshot("/Users/mac/Desktop/Project/Crawling/kream_screenshot/supreme.png")
    # driver.save_screenshot(f"/Users/mac/Desktop/Project/Crawling/kream_screenshot/supreme{i}.png")
    # tag name 선택 가능 
    time.sleep(0.2)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".product_card") 

num = 1
for i in items:
    product_name = i.select_one(".translated_name")
    product_info = i.select_one(".name")
    money = i.select_one(".amount") 
    review = i.select_one(".review_figure")
    wish = i.select_one(".wish_figure")
    if "후드" in product_name.text:
        # 넘버 1부터 시작
        # 브랜드명
        # 제품명
        # 가격
        print(f" 제품 번호는 [{num}]")
        print (f" 제품명(Ko) : {product_name.text}")
        print (f" 제품명(En) : {product_info.text}")
        print (f" 즉시 구매가 : {money.text} ")
        print (f" review : {review.text}개")
        print (f" wish : {wish.text}개")

        print()
        num += 1

    driver.quit()