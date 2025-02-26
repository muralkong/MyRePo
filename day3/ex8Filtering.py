import cv2
import numpy as np

# 필터를 적용할 이미지 읽기
image_path = "mountain.jpg"  # 처리할 이미지 경로
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# 이미지를 제대로 읽었는지 확인
if image is None:
    print("이미지를 찾을 수 없습니다. 경로를 확인하세요!")
else:
    # 평균값 필터 (Blur)
    average_filter = cv2.blur(image, (5, 5))  # 커널 크기는 (5, 5)

    # 샤프닝 필터
    # 샤프닝 커널 생성
    sharpening_kernel = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

    # 라플라시안 필터
    laplacian_image = cv2.Laplacian(image, cv2.CV_64F)
    laplacian_image = cv2.convertScaleAbs(laplacian_image)  # 절대값 변환

    # 이미지 출력
    cv2.imshow("Original Image", image)
    cv2.imshow("Average Filter", average_filter)
    cv2.imshow("Sharpened Image", sharpened_image)
    cv2.imshow("Laplacian Filter", laplacian_image)

    # 키 입력 대기 후 창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()