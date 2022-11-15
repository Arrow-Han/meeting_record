import cv2
import face_recognition
import numpy as np
import os
import threading


# 好像是可以直接导入的
def multi_face_recognition():
    print('hanxinjiang')

    def nothing():
        pass

    # 说话检测
    def mouse_detect(top, bottom):
        if (bottom[3][1] - top[3][1]) >= 22:
            name_status = 'open'
        else:
            name_status = 'close'

        return name_status

    video_capture = cv2.VideoCapture("../document/mp4_outpyut_test-video.mp4")
    frames_of_video = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    loop_flag = 0
    pos = 0
    cv2.createTrackbar('time', 'demo_video', 0, frames_of_video, nothing)
    # Load a sample picture and learn how to recognize it.
    man_image = face_recognition.load_image_file("../document/speaker_man.png")
    man_face_encoding = face_recognition.face_encodings(man_image)[0]

    # Load a second sample picture and learn how to recognize it.
    woman_image = face_recognition.load_image_file("../document/speaker_woman.png")
    woman_face_encoding = face_recognition.face_encodings(woman_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [
        man_face_encoding,
        woman_face_encoding
    ]
    known_face_names = [
        "man",
        "woman"
    ]
    fras = 0
    while True:
        # 创建视频进度条
        # if loop_flag == pos:
        #     loop_flag = loop_flag + 1
        #     cv2.setTrackbarPos('time', 'demo_video', loop_flag)
        # else:
        #     pos = cv2.getTrackbarPos('time', 'demo_video')
        #     loop_flag = pos
        #     video_capture.set(cv2.CAP_PROP_POS_FRAMES, pos)

        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces and face enqcodings in the frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_landmarks_list = face_recognition.face_landmarks(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # 获取嘴唇的点位
        for landmarks in face_landmarks_list:
            top_lip = landmarks['top_lip']
            print(top_lip)
            bottom_lip = landmarks['bottom_lip']
            print(bottom_lip)
        # Loop through each face in this frame of video
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # 在名字下方显示speaker的说话状态
            mouse_state = str(mouse_detect(top_lip, bottom_lip))
            cv2.rectangle(frame, (left, bottom + 30), (right, bottom), (0, 0, 255), cv2.FILLED)
            cv2.putText(frame, mouse_state, (left, bottom + 30), font, 1.0, (255, 0, 0), 2, cv2.LINE_AA)

        fras = fras + 1
        print("当前帧", fras)
        # Display the resulting image
        cv2.imshow('demo_video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

    return 000


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
            cv2.imwrite(outputDirName + '\\' + str(times) + '.jpg', image)
    print('图片提取结束')
    videos.release()


# 对视频进行抽帧处理
# extract_frame方法的入参分别为：
# 输入视频地址、输出视频地址、视频fps、视频分辨率宽、视频分辨率高、视频需要抽掉的起始帧、视频需要抽掉的结束帧。
# 下面是使用opencv对视频中间几帧抽取的方法。
# 主要的思路是在读取frame的时候，顺便把帧写下来。
# 同时如果不是需要抽取剔除的帧，直接continue到下个循环。
# 样例代码如下，主要按照MP4格式进行处理。
def extract_frame(video_path: str, result_path: str, fps, weight, height, start, end):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    videoWriter = cv2.VideoWriter(result_path, fourcc, fps, (weight, height))
    vc = cv2.VideoCapture(video_path)
    if vc.isOpened():
        ret, frame = vc.read()
    else:
        ret = False
    count = 0  # count the number of pictures
    while ret:
        ret, frame = vc.read()
        if start <= count <= end:
            count += 1
            continue
        else:
            videoWriter.write(frame)
            count += 1
    print(count)
    videoWriter.release()
    vc.release()


if __name__ == '__main__':
    input_dir = r'../document'
    save_dir = r'../document'
    count = 0
# for video_name in os.listdir(input_dir):
#     video_path = os.path.join(input_dir, video_name)
#     outPutDirName = os.path.join(save_dir, video_name[:-4])
#     threading.Thread(target=video_to_frames, args=(video_path, outPutDirName)).start()
#     count = count + 1
#     print('%s th videos has been finished !!!' % count)
