''' @File :permission.py @Author:张宇 @Date :2020/7/28 10:32 @Desc : '''

import functools
from django.shortcuts import redirect,reverse

def dashboard_auth(func):
    @functools.wraps(func)
    def wrapper(self,request,*args,**kwargs):
        user = request.user
        if not user.is_authenticated or not user.is_superuser:
            return redirect('{}?to={}'.format(reverse('login'),request.path))

        return func(self,request,*args,**kwargs)

    return wrapper