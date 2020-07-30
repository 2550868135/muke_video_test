''' @File :common.py @Author:张宇 @Date :2020/7/29 14:57 @Desc : '''
import django
django.setup()
from django.conf import settings
import os
import time
import shutil
from app.tasks.fin_t import video_task
from app.model.video import Video,VideoSub

def check_and_get_video_type(type_obj, type_value, message):
    try:
        type_obj(type_value)
    except:
        return {'code': -1, 'msg': message}

    return {'code': 0, 'msg': 'success'}


def remove_path(paths):
    for path in paths:
        if os.path.exists(path):
            os.remove(path)


def handle_video(video_file, video_id, number):
    in_path = os.path.join(settings.BASE_DIR, 'app/dashboard/temp_in')
    out_path = os.path.join(settings.BASE_DIR, 'app/dashboard/temp_out')
    name = '{}_{}'.format(int(time.time()), video_file.name)
    path_name = '/'.join([in_path, name])

    # 拿到文件上传后的临时路径
    temp_path = video_file.temporary_file_path()
    # python的模块,将temp_path的文件复制到path_name中
    shutil.copyfile(temp_path, path_name)

    out_name = '{}_{}'.format(int(time.time()), video_file.name.split('.')[0])
    video_file_name = out_name
    out_path = '/'.join([out_path,out_name])
    out_name = '.'.join([out_path, 'mp4'])
    command = 'ffmpeg -i {} -c copy {}.mp4'.format(path_name,out_path)

    video = Video.objects.get(pk=video_id)
    video_sub = VideoSub.objects.create(
        video=video,
        url='',
        number=number
    )

    video_task.delay(command,out_name,path_name,video_file_name,video_sub.id)
    #hello.delay()
    return True