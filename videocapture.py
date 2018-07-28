import cv2

cap = cv2.VideoCapture('Model.mp4')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    key = cv2.waitKey(2)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
