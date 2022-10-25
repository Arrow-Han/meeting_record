
import cv2
import os


def get_frame_from_video(video_path, interval):
    """
           video_name:输入视频路径（除了视频名称之外，读入视频的绝对路径中文件夹一定不要出现中文字符，不然不能保存图片）
           interval: 保存图片的帧率间隔
    """
    # 创建存帧文件夹
    path = os.getcwd() + '\\frame\\'
    # pwd = os.getcwd() + '\\frame\\' + "\\video1\\"
    if not os.path.exists(path):
        os.mkdir(path)
        print("directory made")
    # elif not os.path.exists(pwd):
    #     os.mkdir(pwd)
    else:
        print("directory existed")

    video_capture = cv2.VideoCapture(video_path)

    frame_nums = video_capture.get(7)  # 获取视频总帧数
    print("视频的总帧数为：", int(frame_nums))
    frame_rete = video_capture.get(5)  # 获取视频帧率
    print("视频的帧率为：", int(frame_rete))

    i = 0  # i 从 0 开始计数的帧数
    j = 0  # j 从 1 开始，记录第几次间隔

    while True:
        success, frame = video_capture.read()  # 一直在读入视频画面帧
        i += 1
        # 判断帧率间隔保存帧
        if i % interval == 0:
            j += 1
            save_name = path + str(i) + '.jpg'
            cv2.imwrite(save_name, frame)
            print('image of %s is saved' % (save_name))
        if not success:
            print('%s frames saved from the video' % j)
            break


if __name__ == '__main__':
    # 视频路径:（除了视频名称之外，读入视频的绝对路径中文件夹一定不要出现中文字符，不然不能保存图片）
    video_path = r'../../docu/video.mp4'
    interval = 5
    get_frame_from_video(video_path, interval)  # " interval  "  指的是一秒几帧



