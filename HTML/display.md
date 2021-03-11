# display

## layout 정의에 이용

> block, inline, inline-block, none

## block 요소

- 항상 새로운 라인에서 시작
- 가로폭 차지
- div, h1~h6, p, ol, ul, li, hr, table, form

## inline

- content 너비만큼 wrap 되는 성질
- **width, height, margin-top, margin-bottom 지정 불가**
- span, a, strong, img, br, input, select, textarea, button
- 상, 하 여백은 line-height로 지정

## inline-block

- **한 줄에 표현되면서 width, height, margin 지정 가능**
- content의 너비만큼 가로폭을 차지

---

## 관련 속성

### visibility  

- 요소를 보이게 하느냐 안 보이게 하느냐
- display: none;은 요소의 공간을 없애지만
- visibility: hidden;은 요소를 보이지만 않게 함

### opacity  

- 투명도를 정의한다
- 0.0~1.0
- 0.0 은 투명, 1.0은 불투명
