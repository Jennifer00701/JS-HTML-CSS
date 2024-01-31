import requests
# impor -> import 문 은 외부 모듈의 함수, 클래스, 변수를 현재 스크립트 또는 모듈로 가져올 수 있음
# import requests는 파이썬에서 외부 라이브러리인 requests를 현재 스크립트 또는 모듈로 가져오는 데 사용되는 구문

from bs4 import BeautifulSoup

url = "https://www.naver.com/"
# 접속하고자 하는 주소 입력 

req = requests.get(url)
# get 방식을 이용해서 서버에게 resource(자원)을 보내도록 요청 
# 후에 수신할 수 있게 준비됨 -> 데이터 수신이 가능하게 됨 
# requests -> 처음에 사용되며 이후에는 잘 사용되질 않음 정적인 사이트에서는 html 코드 변하지 않기 때문
# requests -> 넘어오는 내용을 마우스 오른쪽 버튼을 누르고 페이지 소스보기로 보이는 내용과 동일


html = req.text
#get 방식을 통해 가져온 데이터 중 우리가 필요한 건 텍스트 형태의 자료다 (가장중요한HTML포함)
# text 만 뽑은 내용 

soup = BeautifulSoup(html, "html.parser")
# BeautifulSoup 이라는 함수는 2가지 파라미터를 넣는데 html, "html.parser"을 넣는다
# ** parser 분석 -> 트리구조로 변경 (컴퓨터가 이해할 수 있게)

query = soup. select_one ("#query")
# 지도 안에서 이걸 찾아줘 -> id값인 query 를 찾아라 
# select_one 아이디 태그 안 모든 값 가져오기
# selete_one 으로 원하는 태그를 찾을 수 있다 (기준은 클래스명 or ID, 태그 가능)
    # 클래스의 경우는 앞에 점(.), 아이디 (#)을 붙인다 css 동일 

print(query)

# HTTP 요청 보내기:

# requests.get(url): 지정된 URL로 GET 요청을 보내고 해당 URL에서 받은 응답을 반환
# requests.post(url, data): 지정된 URL로 POST 요청을 보내고 데이터를 함께 전송

# response.text: 서버로부터 받은 응답 데이터를 문자열 형태로 얻음
# response.json(): JSON 형식의 응답을 파이썬 딕셔너리나 리스트로 파싱
# 요청에 대한 다양한 옵션 설정:
# params: 쿼리 문자열 매개변수를 추가하여 GET 요청을 보낼 수 있음
# headers: 요청 헤더를 지정하여 사용자 에이전트나 인증 토큰을 설정할 수 있음
# data: POST 요청 시 데이터를 전송할 수 있음
# cookies: 쿠키를 설정하거나 읽어올 수 있음


