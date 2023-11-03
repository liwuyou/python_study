import cv2 as cv
import numpy as np

img = cv.imread("img/1 (1).jpg")
print(img.shape)
print(img.shape[0])
# 打印出(1526, 1080, 3)
# 打印出的分别是，高，宽，BGR

# 图像大小调整，参数为宽，高
a = int(img.shape[1]*0.3)
b = int(img.shape[0]*0.3)
imgResize = cv.resize(img, (a, b))
print(imgResize.shape)

# 图像裁剪 高与宽
imgCropped = img[0:400, 200:400]


cv.imshow("LOCAL img", img)
cv.imshow("LOCAL imgResize", imgResize)
cv.imshow("LOCAL imgCropped", imgCropped)

cv.waitKey(0)
