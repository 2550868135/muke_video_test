''' @File :base.py @Author:张宇 @Date :2020/7/27 17:57 @Desc : '''
from django.views import View
from app.libs.base_render import render_to_response

class Base(View):
    TEMPLATE = 'base.html'

    def get(self,request):

        return render_to_response(request,self.TEMPLATE)