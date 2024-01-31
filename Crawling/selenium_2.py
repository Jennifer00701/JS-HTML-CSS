from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

url = "https://section.cafe.naver.com/ca-fe/home"

driver = webdriver.Chrome()
driver.get(url) # req = requests.get(url)
html = driver.page_source  # html = req.text 
time.sleep(3)
print(html)