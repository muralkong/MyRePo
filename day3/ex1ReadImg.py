import cv2  # OpenCV 라이브러리 임포트

# Lenna.png 이미지 읽기
image = cv2.imread('Lenna.png',cv2.IMREAD_GRAYSCALE)

# 이미지가 제대로 로드되었는지 확인
if image is None:
    print("이미지를 찾을 수 없습니다. 경로를 확인해주세요.")
else:
    # 이미지 출력
    cv2.imshow('Lenna Image', image)

    # 키 입력 대기 (0은 무한 대기)
    cv2.waitKey(0)

    # 모든 창 닫기
    cv2.destroyAllWindows()