import cv2 as cv
import numpy as np

aaa = np.ones((5, 5), np.uint8)

# cv.imread("路径"， 参数)，参数不传，默认参数1
img = cv.imread("img/1 (1).jpg")

# cv2.namedWindow(‘窗口标题’,默认参数) 创建新窗口
cv.namedWindow('Local Camera', 0)
# 设置显示的窗口大小为500,500，建议大于等于摄像头分辨率
cv.resizeWindow("Local Camera", 300, 300)
cv.imshow("Local Camera", img)

# 灰度图片
imgGray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("show imgGray", imgGray)

# 高斯模糊
imgBlur = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("show imgBlur", imgBlur)

# 边缘检测
imgCanny = cv.Canny(img, 150, 200)
cv.imshow("show imgCanny", imgCanny)

# 膨胀
imgDilation = cv.dilate(imgCanny, aaa, iterations=1)
cv.imshow("show imgDilation", imgDilation)

# 腐蚀
imgErode = cv.erode(imgDilation, aaa, iterations=1)
cv.imshow("show imgErode", imgErode)
cv.waitKey(0)

