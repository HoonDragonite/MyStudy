# 입력값이 몇 개가 될지 모를 때
def sumOfNumbers(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum
    
print(sumOfNumbers(1,2,3,4,5,6,7,8,9,10))

# 함수는 항상 한 개의 값까지만 리턴할 수 있다.


# Lambda
# lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식


add = lambda x, y: x + y
a = 5
b = 5
print(add(a, b))