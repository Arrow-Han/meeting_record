import numpy as ny
import moviepy.editor as mp
from weblfasr import RequestApi
from speaker_recognition import video_to_frame_use
import cv2
import face_recognition

l_get = []


# 第一部分，输入视频，将视频中的音频提取出来
def extract_audio(videos_file_path):
    my_clip = mp.VideoFileClip(videos_file_path)
    return my_clip


# 第二部分，将音频转化为文字
# 直接调用webfasr中的接口就可以
def get_txt(audio_file_path):
    api = RequestApi(appid="2d4d725a", secret_key="ae4b0a67dfcf8a06a8e63c639eaeeab9",
                     upload_file_path=audio_file_path)
    result = api.all_api_request()
    # 之后将输出的文字转化为一个文件保存到文件夹中
    # 保存数据open函数
    with open('../document/result_txt.txt', 'w', encoding='utf-8') as f:  # 使用with open()新建对象f
        f.write(str(result) + '\n')  # 写入数据，文件保存在上面指定的目录，加\n为了换行更方便阅读
    # 提取当中的有效数据
    # 有效数据存储在l_get中，数据类型为list

    with open('../document/result_txt.txt', 'r', encoding='utf-8') as f:
        s = f.read()
        l_mid = eval(eval(s)['data'])
        # global l_get
        # l_get = l_mid


# 第三部分，导入人脸识别模块，进行人脸识别
# 暂存的修改在test中，还没有修改完成
def multi_face_recognition():
    print(l_get)
    print('hanxinjiang')

    def nothing():
        pass

    video_capture = cv2.VideoCapture("../document/mp4_outpyut_test-video.mp4")
    frames_of_video = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    loop_flag = 0
    pos = 0
    cv2.createTrackbar('time', 'demo_video', 0, frames_of_video, nothing)

    return 000


if __name__ == "__main__":
    # 11-15 already right，please note off while using
    # # part01
    # file_path = r'../document/mp4_output_test-video.mp4'
    # my_clip = extract_audio(file_path)
    # my_clip.audio.write_audiofile(f'../document/video_output.mp3')
    #
    # # part02
    # file_path_audio = r'../document/video_output.mp3'
    # # part03调用之后有return也可以，本函数调用可以省略
    # get_txt(file_path_audio)

    # part03 video to frame
    video_to_frame_use()

    # part04 人脸识别以及进行张嘴检测部分模型调用

    input_path = r"../document/speaker_man.png"
    with open('../document/result_txt.txt', 'r', encoding='utf-8') as f:
        s = f.read()
        l_mid = eval(eval(s)['data'])
        print(l_mid)
        print(type(l_mid))
        l_get = l_mid

    print(l_get)
    print(type(l_get))
    print('-------')
    # for i in l_get:
    #     print(i)
    #     begin_tm = i['bg']
    #     end_tm = i['ed']
    #     print(begin_tm,end_tm)
    test_i = l_get[1]
    print(test_i)
    begin_tm = int(test_i['bg'])
    end_tm = int(test_i['ed'])
    print(begin_tm, type(begin_tm), end_tm, type(end_tm))






