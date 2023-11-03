import cv2

cap = cv2.VideoCapture(0)

print('ok')

cap.set(3, 300)
cap.set(4, 300)  # 设置摄像头分辨率，3为高，4为宽

while True:
    ret, frame = cap.read()

    # cv2.namedWindow(‘窗口标题’,默认参数) 创建新窗口
    cv2.namedWindow('Local Camera', 0)
    # 设置显示的窗口大小为500,500，建议大于等于摄像头分辨率
    cv2.resizeWindow("Local Camera", 300, 300)

    cv2.imshow("Local Camera", frame)

    # 移动当前显示窗口至（0,0）
    # cv2.moveWindow("Local Camera", 0, 0)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
