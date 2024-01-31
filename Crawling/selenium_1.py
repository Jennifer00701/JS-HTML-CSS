from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://www.naver.com/"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
# 3초동안 안 꺼지도록 

# title = driver.title
# print(title)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

query = soup.select_one('#query')
print(query)
