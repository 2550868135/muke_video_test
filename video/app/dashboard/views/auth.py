''' @File :auth.py @Author:张宇 @Date :2020/7/27 21:59 @Desc : '''
from django.views import View
from app.libs.base_render import render_to_response
from django.shortcuts import redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from app.utils.permission import dashboard_auth

class Login(View):
    TEMPLATE = 'dashboard/auth/login.html'

    def get(self, request):
        if request.user.is_authenticated:

            return redirect(reverse('dashboard_index'))
        to = request.GET.get('to', '')
        data = {'error': '','to':to}
        print(to)
        return render_to_response(request, self.TEMPLATE, data)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        to = request.GET.get('to','')

        exists = User.objects.filter(username=username).exists()
        data = {}
        if not exists:
            data['error'] = '用户不存在'
            return render_to_response(request, self.TEMPLATE, data)

        user = authenticate(username=username, password=password)
        if not user:
            data['error'] = '密码错误'
            return render_to_response(request, self.TEMPLATE, data)

        if not user.is_superuser:
            data['error'] = '你无权登录'
            return render_to_response(request, self.TEMPLATE, data)

        login(request, user)
        if to:
            return redirect(to)
        return redirect(reverse('dashboard_index'))


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))


class AdminManger(View):
    TEMPLATE = 'dashboard/auth/admin.html'

    @dashboard_auth
    def get(self, request):
        # users = User.objects.filter(is_superuser=True)
        users = User.objects.all()
        page = request.GET.get('page', '1')
        p = Paginator(users, 2)
        total_page = p.num_pages      #获取总页数
        if int(page) <= 1:
            page = 1
        current_page = p.get_page(int(page)).object_list
        # print(current_page.object_list)
        data = {'users': current_page,'total':total_page,'page_num':int(page)}
        return render_to_response(request, self.TEMPLATE, data=data)


class UpdateAdminStatus(View):
    @dashboard_auth
    def get(self, request):
        status = request.GET.get('status', 'on')
        _status = True if status == 'on' else False

        request.user.is_superuser = _status
        request.user.save()

        return redirect(reverse('admin_manager'))
