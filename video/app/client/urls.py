''' @File :urls.py @Author:张宇 @Date :2020/7/27 16:40 @Desc : '''
from django.urls import path
from .views.base import Index
from .views.video import ExVideo,VideoSub,CusVideo
urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('video/ex/',ExVideo.as_view(),name='client_ex_video'),
    path('video/<int:video_id>',VideoSub.as_view(),name='client_video_sub'),
    path('video/custom',CusVideo.as_view(),name='client_cus_video')
]