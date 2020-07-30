''' @File :video.py @Author:张宇 @Date :2020/7/30 21:08 @Desc : '''

from django.views.generic import View
from app.libs.base_render import render_to_response
from app.model.video import Video,FromType
from django.shortcuts import render,reverse,get_object_or_404

class ExVideo(View):
    TEMPLATE = 'client/video/video.html'
    def get(self,request):
        videos = Video.objects.exclude(from_to=FromType.custom.value)
        data = {'videos':videos}
        return render_to_response(request,self.TEMPLATE,data)

class VideoSub(View):
    TEMPLATE = 'client/video/video_sub.html'

    def get(self,request,video_id):
        video = get_object_or_404(Video,pk=video_id)
        data = {'video':video}

        return render_to_response(request,self.TEMPLATE,data=data)


class CusVideo(View):
    TEMPLATE = 'client/video/video.html'

    def get(self, request):
        videos = Video.objects.exclude(from_to=FromType.youku.value)
        data = {'videos': videos}
        return render_to_response(request, self.TEMPLATE, data)