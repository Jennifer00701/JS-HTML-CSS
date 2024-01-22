const form = document.getElementById("form")

form.addEventListener("submit", function(event){
// submit 은 form 에서 제출 이루어진 후 새로고침하는 이벤트 유형 
event.preventDefault() //  기존 기능 차단  (새로고침 안되도록)

let userId = event.target.Id.value
let userPw1 = event.target.Pw1.value
let userPw2 = event.target.Pw2.value
let userName = event.target.Name.value
let userPhone = event.target.Phone.value
let userEmail = event.target.Email.value
let userPosition = event.target.Position.value
let userGender = event.target.Gender.value
let userIntro = event.target.Intro.value

// 모든 입력 값 여기서 id 는 name 에 값이다!!!
// 이벤트가 발생항 타깃 (form)으로 부터 입력 요소로부터 값 입력받는다
// form 은 name 을 가지고 접근하게 됨
// 입력 요소 접근 후 값을 읽는게 value

console.log(userId, userPw1, userPw2,userName, userPhone,
    userEmail, userPosition,userGender,userIntro)
// 유저 아이디 콘솔에 확인하기 

if(userId.length < 6) {
    alert("아이디가 너무 짧습니다. 6자 이상으로 입력해주세요")
// 문자 개수가 몇 개인가 숫자를 반환해주는 속성  
    return
// return 함수에서 값이 반환 시 사용 
// 함수를 강제 종료함 / 문제가 발생 시 강제 종료 하겠다 라는 뜻 
}
else {
    alert("아이디가 설정됐습니다.")
}

if(userPw1 !== userPw2) {
    alert("비밀번호가 다릅니다. 다시입력해주세요")
    return
}
else if(userPw1 == userPw2) {
    alert("비밀번호가 설정됐습니다.")
}

document.body.innerHTML = ""
document.write(`<p>${userId}님 환영합니다</p>`)
// innerHTML 이 태그 안 코드를 부르겠다.
// = 에 새로운 HTML 코드를 대입하겠다. "" 아무것도 없는 것 

})






// 제출 이벤트를 받는다 (이벤트 핸들링)
// 제출된 입력 값들을 참조한다
// 입력값에 문제가 있는 경우 이를 감지한다
// 가입 환영 인사를 제공한다
