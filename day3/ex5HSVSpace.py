import cv2

# 이미지를 읽기
image = cv2.imread('Lenna.png')

# 원본 이미지 출력
cv2.imshow('Original', image)

# 이미지를 HSV 색 공간으로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV 성분 분리 (채널 분리)
h, s, v = cv2.split(hsv_image)

# 각 성분을 출력
cv2.imshow('Hue', h)  # 색상(H)
cv2.imshow('Saturation', s)  # 채도(S)
cv2.imshow('Value', v)  # 명도(V)

# 종료 대기
cv2.waitKey(0)
cv2.destroyAllWindows()