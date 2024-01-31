import requests
# requests 패키지를 불러오는 것
# 웹 서버에 HTTP GET 요청을 보내고 해당 요청에 대한 응답을 받아오는 기능
from bs4 import BeautifulSoup
# import BeautifulSoup 패키지 가져와서 그안에서 bs4라는 패키지만 추출
# 정적페이지만 BeautifulSoup 사용 -> 그순간에 요청을 보내 받아온 html 문서 반영

url = "https://www.naver.com/"

req = requests.get(url)
# requests 요청을 url 적힌 주소로 보내기 / 이후 req 변수 만듬
# HTTP 오류 코드 사이트
# (https://developer.mozilla.org/ko/docs/Web/HTTP/Status)

html = req.text
# heml 변수 만들고 req : 요청에 대한 응답을 받아오는 것 text만 추출해줘 
soup = BeautifulSoup(html, "html.parser")
# 위에 만든 변수 html 내용이 soup으로 들어가서 parser 로 컴퓨터가 이해할 수 있는 트리구조를 만듬

query = soup.select_one("#query")
# soup에 parser한 것 중에 내용 query를 찾아줘 
print(query)