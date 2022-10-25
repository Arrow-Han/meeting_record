import face_recognition
import cv2
import numpy as np


def nothing(emp):
    pass


# Get a reference to webcam #0 (the default one)


video_capture = cv2.VideoCapture("../../docu/test_video.MOV")
frames_of_video = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
loop_flag = 0
pos = 0
cv2.createTrackbar('time', 'demo_video', 0, frames_of_video, nothing)

# Load a sample picture and learn how to recognize it.
man_image = face_recognition.load_image_file("../../docu/speaker_man.png")
man_face_encoding = face_recognition.face_encodings(man_image)[0]

# Load a second sample picture and learn how to recognize it.
woman_image = face_recognition.load_image_file("../../docu/speaker_woman.png")
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


# 说话检测
def mouse_detect(top, bottom):
    if (bottom[3][1] - top[3][1]) >= 22:
        name = 'open'
    else:
        name = 'close'

    return name


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