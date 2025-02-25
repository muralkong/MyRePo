def gugudan():
    for i in range(1, 10):  # 1부터 9까지
        for j in range(1, 10):  # 1부터 9까지
            print(f"{i} x {j} = {i * j}")
        print()  # 각 단마다 줄 바꿈


# 함수 실행
gugudan()