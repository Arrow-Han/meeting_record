import face_recognition
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import dlib
import os
import math


# 计算两个坐标的距离
def euclidian_distance(p1, p2):
    diff_x = abs(p2[0] - p1[0])
    diff_y = abs(p2[1] - p1[1])
    return math.sqrt(diff_x * diff_x + diff_y * diff_y)


def mouse_detect(top, bottom):
    if (bottom[3][1] - top[3][1]) >= 22:
        name = 'open'
    else:
        name = 'close'

    return name


path = face_recognition.load_image_file("../docu/speaker_man.png")

# cap = cv.VideoCapture(0)
# fps = cap.get(cv.CAP_PROP_FPS)  # 获取摄像头或者视频帧率
# print(fps)
# count = int(cap.get(7))  # 总帧数
# print("总帧数",count)

face_locations = face_recognition.face_locations(path)
print(face_locations)
print(face_locations[0])
print(len(face_locations))
face_landmarks_list = face_recognition.face_landmarks(path)
print(face_landmarks_list)

# face_recognition的关键点获取
# for landmarks in face_landmarks_list:
#     top_lip = landmarks['top_lip']
#     print(top_lip)
#     bottom_lip = landmarks['bottom_lip']
#     print(bottom_lip)
#     mouse_state = str(mouse_detect(top_lip, bottom_lip))

# dlib关键点获取
# 脸部关键点预测器
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# (mouth_lower, mouth_upper) = face_utils.FACIAL_LANDMARKS_68_IDXS['mouth']
(mouth_lower, mouth_upper) = (48, 60)

ACTIVATION_RATIO = 3.0

color = (0, 0, 255)
actived = False
result = []
sum = 0
j = 0
fras = 0

# 使用 Dlib 的正面人脸检测器 frontal_face_detector
detector = dlib.get_frontal_face_detector()
path_dlib = "../docu/speaker_man.png"
image_man = cv.imread(path_dlib)




faces = detector(image_man, 1)
print('=======')

print(faces)