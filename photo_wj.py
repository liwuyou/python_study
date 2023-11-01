import cv2

cap = cv2.VideoCapture(0)
i = 0
try:
    while True:
        ret, frame = cap.read()
        cv2.imshow('Local Camera', frame)
        k = cv2.waitKey(1)
        if k == ord("Q"):
            break
        elif k == ord("K"):
            # ret, frame = cap.read()
            cv2.imwrite("/home/ucar/photo_wj/photo/" + str(i) + ".jpg", frame)
            i = i + 1
            print("Ok")

except:
    cap.release()
    cv2.destroyAIWindows()
