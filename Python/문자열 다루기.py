# 문자열을 만드는 방법 4가지
print('Hello World!')
print("Hello World!")
print("""Hello World!""")
print('''Hello World!''')
print("\n")

# 따옴표 출력하기
print('큰 따옴표 출력하기 "Hello World!"')
print("작은 따옴표 출력하기 'World'")
print("백슬래시를 이용하여 따옴표를 포함시키기 \"Hello World!\"")
print("\n")

# 문자열 인덱싱
a = "Hello World!"
print(a[0]) # H
print(a[1]) # e
print(a[-1]) # !

# 문자열 슬라이싱, n:m 인덱스 n부터 인덱스 m-1까지를 뽑자
print(a[0:5]) # "Hello"
print(a[6:]) # "World!"
print(a[:]) # "Hello World!"
print(a[0:-1]) # "Hello World"

# 문자열은 immutable하다. 인덱싱하여 값을 변경할 수 없음.
replaceTest = "철수 철수 철1수 짱구 짱구"
replaceResult = replaceTest.replace("철수", "유리")
print(replaceTest + " -> " + replaceResult)
replaceResult = replaceTest.replace("짱구", "훈이", 1)
print(replaceTest + " -> " + replaceResult)