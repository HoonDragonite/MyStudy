# Box Model

## 모든 HTML 요소는 Box 형태의 영역을 갖고 있다.  

### 이 Box는 콘텐트(Content), 패딩(Padding), 테두리(Border), 마진(Margin)으로 구성된다

![box-model](./Image/box-model.png)

### 출처 : <https://poiemaweb.com/css3-box-model>

---

## 속성 : box-sizing

### **box-sizing: content-box** (기본값)

- content + padding + border + margin이 요소의 width
- 이때 width 속성은 content의 너비

### **box-sizing: border-box** (border까지 width에 포함)

- border까지 width 속성에 포함이니 내부 값까지는 생각 안해도 돼서 편하긴 함
- IE8부터 지원, 요새 많이 씀
