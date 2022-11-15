import cv2
import face_recognition
import os
import threading


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
