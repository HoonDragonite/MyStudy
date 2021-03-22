# 자바의 for(int i=0; i<len; i++)형태 쓰고 싶을 때
len = 10
for _ in range(10):
    print("hello")

# 배열 순회
numToTen = list(range(1, 11))
for i in numToTen:
    print(i)

# 짝수, 홀수 리스트 컴프리헨션
evenArr = [i for i in range(1, 11) if i % 2 == 0]
print(evenArr)

# 2차원 리스트 만들기
n = 3
m = 4
array = [[0] * m for _ in range(n)] # 3X4
print(array)

# 특정한 값의 원소 모두 지우기, remove()는 O(n)으로 오래 걸림
arr = [1, 2, 3, 4, 5, 5, 5]
removeArr = [3, 5]

result = [i for i in arr if i not in removeArr]
print(result)

