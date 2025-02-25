a = 5
b = 10
# 더하기 함수
def add(x, y):
    return x + y


# 빼기 함수
def subtract(x, y):
    return x - y


# 곱하기 함수
def multiply(x, y):
    return x * y


# 나누기 함수
def divide(x, y):
    if y == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return x / y


# 사용 예시
a = 5
b = 10

print("더하기:", add(a, b))
print("빼기:", subtract(a, b))
print("곱하기:", multiply(a, b))
print("나누기:", divide(a, b))