import cv2

# 카메라 열기(기본 카메라는 인덱스 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

while True:
    # 카메라에서 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽어올 수 없습니다. 종료합니다.")
        break

    # 프레임 출력
    cv2.imshow('Camera', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()