''' @File :fin_t.py @Author:张宇 @Date :2020/7/30 17:55 @Desc : '''
''' @File :ts.py @Author:张宇 @Date :2020/7/30 17:53 @Desc : '''
import django
django.setup()
from celery import task
from app.libs.base_qiniu import video_qiniu
import os
from app.model.video import VideoSub


@task
def video_task(command,out_name,path_name,video_file_name,video_sub_id):
    from app.utils.common import remove_path
    os.system(command)

    if not os.path.exists(out_name):
        remove_path([out_name, path_name])
        return False

    url = video_qiniu.put(video_file_name, out_name)
    if url:
        try:
            video_sub = VideoSub.objects.get(pk=video_sub_id)
            video_sub.url = url
            video_sub.save()
            return True
        except :
            return False
        finally:
            remove_path([out_name, path_name])
    return True