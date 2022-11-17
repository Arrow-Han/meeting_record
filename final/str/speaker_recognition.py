import cv2
import face_recognition
import os
import threading
import numpy as np


def video_to_frames(video_path, outputDirName):
    times = 0

    # 提取视频的帧率，每1帧提取一个
    frame_frequency = 1

    # if no path,create
    if not os.path.exists(outputDirName):
        os.makedirs(outputDirName)

    # read frames
    videos = cv2.VideoCapture(video_path)

    while True:
        times = times + 1
        res, image = videos.read()
        if not res:
            print('not res, not image')
            break
        if times % frame_frequency == 0:
            cv2.imwrite(outputDirName + '//' + str(times) + '.jpg', image)
    print('图片提取结束')
    videos.release()


def video_to_frame_use():
    input_dir = r'../document/video'
    save_dir = r'../document/video'
    count = 0
    for video_name in os.listdir(input_dir):
        if video_name == '.DS_Store':
            continue
        video_path = os.path.join(input_dir, video_name)
        outPutDirName = os.path.join(save_dir, video_name[:-4])
        threading.Thread(target=video_to_frames, args=(video_path, outPutDirName)).start()
        count = count + 1
        print('%s th videos has been finished !!!' % count)


def multi_speaker_reg():
    print('begin')

    def nothing(emp):
        pass

    # Load a sample picture and learn how to recognize it.
    no01_image = face_recognition.load_image_file("../../docu/speaker_man.png")
    no01_face_encoding = face_recognition.face_encodings(no01_image)[0]

    # Load a second sample picture and learn how to recognize it.
    no02_image = face_recognition.load_image_file("../../docu/speaker_woman.png")
    no02_face_encoding = face_recognition.face_encodings(no02_image)[0]
    # Create arrays of known face encodings and their names
    known_face_encodings = [
        no01_face_encoding,
        no02_face_encoding
    ]
    known_face_names = [
        "man",
        "woman"
    ]

    # 初始化张嘴状态为闭嘴
    mouth_status_open = 0

    def getFaceEncoding(src):
        image = face_recognition.load_image_file(src)  # 加载人脸图片
        # 获取图片人脸定位[(top,right,bottom,left )]
        face_locations = face_recognition.face_locations(image)
        img_ = image[face_locations[0][0]:face_locations[0][2], face_locations[0][3]:face_locations[0][1]]
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
        # display(img_)
        face_encoding = face_recognition.face_encodings(image, face_locations)[0]  # 对人脸图片进行编码
        return face_encoding

    def simcos(a, b):
        a = np.array(a)
        b = np.array(b)
        dist = np.linalg.norm(a - b)  # 二范数
        sim = 1.0 / (1.0 + dist)  #
        return sim
    def comparison(face_src1, face_src2):
        xl1 = getFaceEncoding(face_src1)
        xl2 = getFaceEncoding(face_src2)
        value = simcos(xl1, xl2)
        print(value)



