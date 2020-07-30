''' @File :base.py @Author:张宇 @Date :2020/7/30 20:33 @Desc : '''
from django.views.generic import View
from django.shortcuts import redirect,reverse

class Index(View):
    TEMPLATE = 'client/base.html'
    def get(self,request):
        return redirect(reverse('client_ex_video'))