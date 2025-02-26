import cv2
import numpy as np

# 1. 이미지 읽기
image = cv2.imread('candies.png')  # candies.png 파일 읽기

# 2. 이미지 BGR to HSV 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 3. RED 성분의 HSV 범위 설정 (두 RED 영역)
lower_red1 = np.array([0, 120, 70])  # Hue가 낮은 빨강색
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 120, 70])  # Hue가 높은 빨강색
upper_red2 = np.array([180, 255, 255])

# 4. RED 영역에 대한 마스크 생성
mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)  # 두 영역의 마스크 결합

# 5. 빨간 영역만 추출된 HSV 이미지 생성
red_only_hsv = cv2.bitwise_and(hsv_image, hsv_image, mask=red_mask)

# 6. 결과 시각화
cv2.imshow("HSV Image (Original)", hsv_image)  # HSV 원본 이미지
cv2.imshow("Red Components (HSV)", red_only_hsv)  # HSV에서 빨간 성분만 표시

# 'q'를 누르면 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()