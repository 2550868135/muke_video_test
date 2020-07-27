''' @File :auth.py @Author:张宇 @Date :2020/7/27 21:59 @Desc : '''
from django.views import View
from app.libs.base_render import render_to_response
from django.shortcuts import redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

class Login(View):
    TEMPLATE = 'dashboard/auth/login.html'

    def get(self,request):
        return render_to_response(request,self.TEMPLATE)

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        exists = User.objects.filter(username=username).exists()
        data = {}
        if not exists:
            data['error'] = '用户不存在'
            return render_to_response(request,self.TEMPLATE,data)

        user = authenticate(username=username,password=password)
        if not user:
            data['error'] = '密码错误'
            return render_to_response(request, self.TEMPLATE, data)

        return redirect('/dashboard/login')