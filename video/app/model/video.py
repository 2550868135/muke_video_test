''' @File :video.py @Author:张宇 @Date :2020/7/28 11:18 @Desc : '''
from enum import Enum
from django.db import models


class VideoType(Enum):
    movie = 'movie'
    cartoon = 'cartoon'
    episode = 'episode'
    variety = 'variety'
    other = 'other'

VideoType.movie.label = '电影'
VideoType.cartoon.label = '动漫'
VideoType.episode.label = '剧集'
VideoType.variety.label = '综艺'
VideoType.other.label = '其他'

class FromType(Enum):
    youku = 'youku'
    custon = 'custom'

FromType.youku.label = '优酷'
FromType.custon.label = '自制'


class NationalityType(Enum):
    china = 'china'
    japan = 'japan'
    korea = 'korea'
    america = 'america'
    other = 'other'

NationalityType.china.label = '中国'
NationalityType.japan.label = '日本'
NationalityType.korea.label = '韩国'
NationalityType.america.label = '美国'
NationalityType.other.label = '其他'

class Video(models.Model):
    name = models.CharField(max_length=100,null=False)
    image = models.CharField(max_length=500,default='')
    video_type = models.CharField(max_length=50,default=VideoType.other.value)
    from_to = models.CharField(max_length=20,null=False,default=FromType.custon.value)
    nationality = models.CharField(max_length=20,default=NationalityType.other.value)
    info = models.TextField()
    status  = models.BooleanField(default=True,db_index=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name','video_type','from_to','nationality')

    def __str__(self):
        return self.name

