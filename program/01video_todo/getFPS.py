import cv2 as cv
import os
import glob

# 获取视频帧率的一个文件
videoCapture = cv.VideoCapture("../docu/test_video.MOV")  #视频路径
fps = videoCapture.get(5)
print(fps)
frames_num = videoCapture.get(7)
print(frames_num)