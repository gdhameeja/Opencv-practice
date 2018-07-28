import cv2

cap = cv2.VideoCapture('Model.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('output.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:

        print(frame)
        
        writer.write(frame)
        cv2.imshow('frame', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
writer.release()
            
