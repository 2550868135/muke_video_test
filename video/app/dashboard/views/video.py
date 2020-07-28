''' @File :video.py @Author:张宇 @Date :2020/7/28 21:01 @Desc : '''
from django.views import View
from app.libs.base_render import render_to_response
from django.shortcuts import reverse,redirect
from app.utils.permission import dashboard_auth

class ExternalVideo(View):
    TEMPLATE = 'dashboard/video/external_video.html'

    @dashboard_auth
    def get(self,request):
        return render_to_response(request,self.TEMPLATE)