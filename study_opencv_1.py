# 学习了基本操作，imread(), imwrite()等
import cv2 as cv

# 获取摄像头
cap = cv.VideoCapture(0)
# set the height(3) and width(4) of the windows
# windows系统下，微软surface的系统摄像头，该设置失效，原因未明
# 外置摄像头OK
cap.set(3, 640)
cap.set(4, 480)

# set brightness
# 但好像也没什么用
cap.set(10, 0.00001)

while True:
    success, img = cap.read()

    cv.imshow("camera", img)
    if cv.waitKey(1) == ord('Q') or cv.waitKey(1) == 27:

        # 当所有事完成，释放 VideoCapture 对象
        cap.release()
        cv.destroyAllWindows()
        break



