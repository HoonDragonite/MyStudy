# position

> 요소의 위치를 정의

## static
- position 프로퍼티의 기본 값.
- position 프로퍼티를 지정하지 않았을 때와 같다.
- 부모 요소의 위치를 기준으로

## relative
- 기본 위치를 기준으로 top, bottom, left, right로 위치 이동
- 안드로이드의 constraint layout과 비슷한 것 같다.

## absolute
- 부모 요소 또는 가장 가까이 있는 조상 요소(static 제외)를 기준
-  relative, absolute, fixed 등의 부모 또는 조상 요소가 있어야 한다.
  
### relative와 absolute의 차이점
- relative 기본 위치를 기준으로 위치를 이동 (무조건 부모를 기준)
- absolute 부모에 static 외에 속성이 있어야만 부모를 기준으로 위치
- parent가 없다면 그냥 static에 위치 하는 것 같다.

## fixed

- 브라우저의 viewport를 기준으로 위치함
- 스크롤이 되더라도 화면에서 사라지지않음

 ##### block 요소에 absolute 혹은 fixed 선언 시 width는 inline 요소와 같이 content에 맞게 변화되므로 적절한 width를 지정하여야 한다.

 <br>

 ---

 <br>

 ## z-index
- 큰 값을 지정할 수록 화면 전면에 출력
- 한글 문서의 앞에 보이기 속성과 같다
- z-index: 1, z-index:2, z-index:3 이 있을 때 3인게 제일 위에 위치

## overflow 속성
- 자식 요소가 부모 요소를 벗어났을 때 처리 방법을 정의
- overflow, overflow-x, overflow-y
  
<table>
    <th>
        <td>속성</td>
        <td>설명</td>
    </th> 
    <tr>
        <td></td>
        <td>visible</td>
        <td>영역을 벗어난 부분을 표시(기본값)</td>
    </tr>
    <tr>
        <td></td>
        <td>hidden</td>
        <td>벗어난 부분은 잘림</td>
    </tr>
    <tr>
        <td></td>
        <td>scroll</td>
        <td>벗어난 부분이 없어도 스크롤 표시</td>
    </tr>
    <tr>
        <td></td>
        <td>auto</td>
        <td>벗어난 부분이 있으면 스크롤 표시(대부분 브라우저)</td>
    </tr>
</table>
