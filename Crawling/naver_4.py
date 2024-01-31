import requests
from bs4 import BeautifulSoup
# requests, BeautifulSoup 모듈을 임포드 함
# requests 모듈은 웹 페이지에 HTTP 요청을 보내고 응답을 받기 위해 사용
# BeautifulSoup 모듈은 HTML 문서를 파싱하고 원하는 정보를 추출하는 데 사용


header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
# 사용자 에이전트(User-Agent) 헤더를 정의
# 이 헤더는 웹 서버에게 요청이 웹 브라우저에서 온 것처럼 보이도록 하는 역할을 함
# 이를 통해 웹 스크래핑을 할 때 차단을 피할 수 있음

base_user = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
# 검색을 위한 naver 기본 URL(검색페이지) 정의

search_url = input("검색어를 입력해주세요")
# input 함수를 사용하여 검색어를 입력받고, search_url 변수에 저장

url = base_user + search_url
# 입력받은 검색어를 base_user와 조합하여 검색 URL을 생성하고, url 변수에 저장

req =requests.get(url, headers = header_user)
# requests 모듈을 사용하여 해당 URL에 GET 요청을 보냄
# requests.get(url, headers=header_user)을 
# 사용하여 Naver의 검색 페이지에 요청을 보내고, 응답을 req 변수에 저장

html = req.text
# req.text를 사용하여 서버 응답의 HTML 내용을 문자열로
# 가져와서 html 변수에 저장

soup = BeautifulSoup(html, "html.parser")
# 컴퓨터가 알 수 있게 트리 구조로 만든 것

title = soup.select(".title_link._cross_trigger")
# search_one 을 쓰면 하나만 가져오기 
name = soup.select(".user_info > a")
# 유저인포 다음에 나오는 a 태그 지칭
# 정보를 이용해서 추출해온 데이터를 리스트 형태로 공간 하나씩 가져오는 것 

for i in zip (title, name) :
    # zip -> title , name 인덱싱 0번 값 묶기 : 출력 결과는 tuple 형태
    print(type)
    print(f"블로그 글 제목 : {i[0]}") # title, name 
    print(f"블로그 내용 : {i[1].text}")
    print(f"블로그 링크 : {i[0]['href']}")
    print()