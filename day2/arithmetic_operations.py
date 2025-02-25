# 상수 정의
ERROR_DIVIDE_BY_ZERO = "0으로 나눌 수 없습니다."


# 0으로 나누는지 확인하는 함수
def validate_non_zero_divisor(y):
    if y == 0:
        raise ValueError(ERROR_DIVIDE_BY_ZERO)


# 덧셈 함수
def add_numbers(x, y):
    return x + y


# 나눗셈 함수
def divide_numbers(x, y):
    validate_non_zero_divisor(y)
    return x / y


# 제곱 함수
def power_numbers(x, y):
    return x ** y


# 나머지 연산 함수
def mod_numbers(x, y):
    return x % y


# 곱셈 함수
def multiply_numbers(x, y):
    return x * y


# 뺄셈 함수
def subtract_numbers(x, y):
    return x - y

# 상수 정의
ADD_LABEL = "더하기"
SUB_LABEL = "빼기"
MUL_LABEL = "곱하기"
DIV_LABEL = "나누기"
POW_LABEL = "POWER"
MOD_LABEL = "MOD"


# 수학 연산 함수 정의
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2 if num2 != 0 else "나눌 수 없습니다"


def power(num1, num2):
    return num1 ** num2


def mod(num1, num2):
    return num1 % num2 if num2 != 0 else "나눌 수 없습니다"


# 사용 예시
num1 = 5
num2 = 10
print(f"{ADD_LABEL}: {add(num1, num2)}")
print(f"{SUB_LABEL}: {subtract(num1, num2)}")
print(f"{MUL_LABEL}: {multiply(num1, num2)}")
print(f"{DIV_LABEL}: {divide(num1, num2)}")
print(f"{POW_LABEL}: {power(num1, num2)}")
print(f"{MOD_LABEL}: {mod(num1, num2)}")