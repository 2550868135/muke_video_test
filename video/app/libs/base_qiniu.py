''' @File :base_qiniu.py @Author:张宇 @Date :2020/7/30 9:50 @Desc : '''
from qiniu import Auth, put_data, put_file
# put_data是上传二进制文件,put_file是上传本地的文件
from django.conf import settings

class Qiniu(object):
    def __init__(self,bucket_name,base_url):
        # 存储空间名
        self.bucket_name = bucket_name
        # 外链域名
        self.base_url = base_url
        self.q = Auth(settings.QINIU_AK,settings.QINIU_SK)

    def put(self,name,path):
        token = self.q.upload_token(self.bucket_name,name)
        ret,info = put_file(token,name,path)

        if 'key' in ret:
            #获得完整的链接
            remote_url = '/'.join([self.base_url,ret['key']])
            #访问的链接
            return  remote_url


video_qiniu = Qiniu(bucket_name=settings.QINIU_VIDEO,
                    base_url=settings.QINIU_VIDEO_URL)
