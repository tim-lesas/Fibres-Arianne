import cv2

cap = cv2.VideoCapture("Enregistrements\\Videos_20230522_155825\\20230522_155825_Kinect_7.mkv")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    cv2.putText(frame, "Hello world", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 25, (0, 0, 255))

    cv2.imshow('Video', frame)

    if cv2.waitKey(16) & 0xFF == ord('q'): # Lis la video à 60 fps
        break

cap.release()
cv2.destroyAllWindows()
