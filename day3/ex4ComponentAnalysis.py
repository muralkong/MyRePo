import cv2

# 이미지 읽기
image = cv2.imread('Lenna.png')

# 이미지가 제대로 읽혔는지 확인
if image is None:
    print("이미지를 읽을 수 없습니다. 파일 경로를 확인하세요.")
    exit()

# 이미지의 B, G, R 채널 분리
b, g, r = cv2.split(image)

# 각 채널 출력
cv2.imshow('Blue Channel', b)
cv2.imshow('Green Channel', g)
cv2.imshow('Red Channel', r)

# 원본 이미지 출력
cv2.imshow('Original Image', image)

# 키 입력 대기 (아무 키나 누르면 종료)
cv2.waitKey(0)

# 모든 창 닫기
cv2.destroyAllWindows()