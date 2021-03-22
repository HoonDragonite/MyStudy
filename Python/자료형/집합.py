# 집합 {} 키가 없고 값만 존재
# 순서가 없다, unique한 값을 가진다.

s = {1, 2, 3}
s.add(4)
print(s)

s2 = set([1, 3, 5, 7, 7, 7, 7])
print(s2) # {1, 3, 5, 7}

# d.update 값을 한 번에 추가
s.update({3, 4, 5})
print(s)

# d.remove 찾는 자료가 없으면 에러발생 
# d.discard 찾는 자료가 없으면 에러발생x

# 합집합 |
# 교집합 &
# 차집합 -