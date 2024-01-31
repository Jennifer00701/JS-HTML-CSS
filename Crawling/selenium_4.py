from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# 여러가지 옵션들 들어있는 것을 작동할 수 있는 코드를 변수에 넣음

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# 유저 정보 넣기
options.add_argument(f"User-Agent={user}")

#화면 자동 종료 해제 옵션
options.add_experimental_option("detach", True)

# 화면 크기 설정 (최대 크기로 설정)
options.add_argument("--start-maximized")
# f11 눌렀을 때 풀 화면 
# options.add_argument("--start-fullscreen")
# 윈도우 사이즈 조정  
# options.add_argument("window-size=500, 500")

# 브라우저 화면이 나오지 않은 상태에서 크롤링 작업하게 만들어주는 옵션 
# options.add_argument("--headless")

# 상단에 조작되고 있다는 메시지 지우는 옵션
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# 시크릿모드
options.add_argument("incognito")
driver = webdriver.Chrome(options=options)
url = "https://naver.com"
driver.get(url)
