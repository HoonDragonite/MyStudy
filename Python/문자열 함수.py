# format() 값을 대입하는 함수
# {idx} 순서대로 format() 함수로 채워넣음
print("{0} days. And {1} times".format(7, 24)) 
print("My name is {name}".format(name="이름"))

# 문자열 공백으로 채우기
print("%10s" % "right")
print("%-10s" % "left")
print("{0:<10}".format("left"))
print("{0:>10}".format("right"))
print("{0:^10}".format("center"))
print("{0:*^10}".format("center"))

# replace()
replaceTest = "철수 철수 철1수 짱구 짱구"
print("원래 값 : " + replaceTest)
replaceResult = replaceTest.replace("철수", "유리")
print("* 모든 \"철수\"를 유리로    -> " + replaceResult)
replaceResult = replaceTest.replace("짱구", "훈이", 1)
print("* 한 개의 \"짱구\"를 훈이로 -> " + replaceResult)
print("원래 값 : " + replaceTest)

# count()
print("***ab*c*".count("*"))

# find() 문자가 처음 나온 위치
print("12345".find("3"))

# join() 문자 사이사이에 문자를 삽입
print(",".join("abcde"))

# UpperCase -> LowerCase
print("ABC".lower());

# LowerCase -> UpperCase
print("abc".upper());

# trim 기능
print("  Hello  ".strip())

# split : 배열로 반환한다.
splitTest = "강백호 정대만 채치수 서태웅 송태섭"
print(splitTest.split())

