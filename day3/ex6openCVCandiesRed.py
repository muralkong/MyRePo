import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread('Candies.png')

# 이미지를 BGR에서 RGB로 변환 (OpenCV는 기본적으로 BGR로 읽음)
b, g, r = cv2.split(image)

# RED 값이 50 이상인 부분을 마스크로 만듦
red_mask = r >= 150

# 마스크를 사용해 원본 이미지에서 해당 영역만 출력
result = np.zeros_like(image)
result[red_mask] = image[red_mask]

# 결과 시각화
cv2.imshow('Original Image', image)
cv2.imshow('Red Components >= 50', result)

# 키 입력 대기 후 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()