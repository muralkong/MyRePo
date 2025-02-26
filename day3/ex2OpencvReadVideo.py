import cv2

# 동영상 파일 경로
video_path = 'test_video.mp4'

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(video_path)

# 동영상 파일 열기 확인
if not cap.isOpened():
    print("Error: 비디오 파일을 열 수 없습니다.")
    exit()

# 프레임 읽고 보여주기
while True:
    ret, frame = cap.read()
    if not ret:  # 더 이상 읽을 프레임이 없으면 종료
        break

    # 프레임을 보여줍니다
    cv2.imshow('Video', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()