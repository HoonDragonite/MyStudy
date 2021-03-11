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
# 문자열은 immutable하다. 인덱싱하여 값을 변경할 수 없음.
a = "Hello World!"
print(a[0]) # H
print(a[1]) # e
print(a[-1]) # !
print("\n")

# 문자열 슬라이싱, n:m 인덱스 n부터 인덱스 m-1까지를 뽑자
print(a[0:5]) # "Hello"
print(a[6:]) # "World!"
print(a[:]) # "Hello World!"
print(a[0:-1]) # "Hello World"
print("\n")

# 문자열 포매팅 : 문자열 안에 값을 대입하기
print("%d개만큼의 사과" % 5)
print("%0.2f" % 3.1415)
print("\n")

# %s 문자열
# %c 문자 1개
# %d 정수
# %f 부동소수
# %o 8진수
# %x 16진수
