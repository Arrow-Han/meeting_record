import face_recognition
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
def main():

    # image = face_recognition.load_image_file("WechatIMG255.jpeg")
    # image = face_recognition.load_image_file("WechatIMG254.jpeg")
    image = face_recognition.load_image_file("../docu/shot/image1.jpg")
    plt.figure('face-recognition')
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.axis('off')
    face_locations = face_recognition.face_locations(image)
    print(face_locations)
    face_landmarks_list = face_recognition.face_landmarks(image)

    # image = np.zeros(image.shape, np.uint8)
    for landmarks in face_landmarks_list:
        chin = landmarks['chin']

        top_lip = landmarks['top_lip']
        print(top_lip)
        print(top_lip[3][1])
        bottom_lip = landmarks['bottom_lip']
        print(bottom_lip)
        print(bottom_lip[3][1])

        pts = np.array(top_lip, np.int32)
        cv.polylines(image, [pts], False, (255, 255, 255), 5)
        pts = np.array(bottom_lip, np.int32)
        cv.polylines(image, [pts], False, (255, 255, 255), 5)

        mouse_state = str(mouse_detect(top_lip, bottom_lip))


    for top, right, bottom, left in face_locations:
        cv.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 5)
        cv.rectangle(image, (left, bottom + 30), (right, bottom), (0, 0, 255), cv.FILLED)
        cv.putText(image, mouse_state, (left, bottom + 30), cv.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2, cv.LINE_AA)

    plt.subplot(1, 2, 2)
    plt.imshow(image)
    plt.axis('off')
    plt.show()

def mouse_detect(top, bottom):
    if (bottom[3][1] - top[3][1]) >= 22:
        name = 'open'
    else:
        name = 'close'

    return name

if __name__ == "__main__":
    main()
