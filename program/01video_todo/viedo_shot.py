import cv2 as cv
import numpy as np

# 定义保存图片函数
def save_image(image, addr, num):
    address = addr + str(num) + '.jpg'
    cv.imwrite(address, image)

# 读取视频文件
videoCapture = cv.VideoCapture("../docu/video.mp4")  #视频路径
# 通过摄像头的方式
# videoCapture=cv2.VideoCapture(1)

# 读帧
success, frame = videoCapture.read()
i = 0
timeF = 18.058 #视频帧率设置
j = 0
while success:
    i = i + 1
    if (i % timeF == 0):
        j = j + 1
        save_image(frame, '../docu/shot/image', j)
        #图片保存目录，需提前建立好一个名为output的文件夹
        print('save image:', i)
    success, frame = videoCapture.read()
