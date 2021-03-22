# 리스트 [] mutable
# 리스트는 다른 자료형의 값들을 요소로 가질 수 있다.

booksan = ["강백호", "정대만", "송태섭", "채치수", "서태웅"]
neungnam = ["윤대협", "강태산", "변덕규", "허태환", "안영수"]

print(booksan[0])
print(booksan[-1])

# 리스트 안의 리스트
teams = ["해남", booksan, ["윤대협", "강태산", "기타등등"]]
print(teams[0])
print(teams[1][1])
print(teams[2])

# 리스트 슬라이싱
# 문자열과 사용법은 동일하나 지정한 범위만큼을 리스트로 다시 리턴한다.
print(booksan[:2])

# 리스트 연산
print(booksan + [" vs "] + neungnam)

# len() 리스트의 길이
print(len(booksan))

# 리스트 요소 삭제
tests = [1, 2, 3, 4, 5]
del tests[3:] # 3 이후 삭제
print(tests)