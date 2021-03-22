# 딕셔너리 {'name':'lsh', 'birth':'0906'} mutable
# Key값은 고유하다.

# 값 추가하기
booksan = {}
booksan["C"] = "채치수"
booksan["PG"] = "송태섭"
booksan["SG"] = "정대만"
booksan["PF"] = "강백호"
booksan["SF"] = "서태웅"
print(booksan)

# 값 삭제하기
test = {'a':1}
del test['a']

# d["Key"] Key로 검색하기, 예외 발생시키니까 지양하고 get() 쓰기
print(booksan["C"])

# d.keys()
print(booksan.keys()) # dict_keys 반환, ver 2.7까지는 List 반환

# d.keys() 응용
for position in booksan.keys():
    print(position)

# d.keys() to List
print(list(booksan.keys()))

# d.values()
print(booksan.values())

# d.values() 응용
for player in booksan.values():
    print(player)

# d.values() to List
print(list(booksan.values()))

# d.items() Key:Value 쌍 얻기
print(booksan.items())

# d.clear() d의 값 모두 지우기

# d.get() Key로 값 얻기
print(booksan.get("C"))
print(booksan.get("ABC", "그런 키 값은 없다"))

# d.update() 값을 수정하고, 없으면 추가한다.
d = {"주장":"채치수"}
d.update({"주장":"송태섭", "감독":"안선생님"}) #{'주장': '송태섭', '감독': '안선생님'}