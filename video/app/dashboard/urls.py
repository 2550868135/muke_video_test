''' @File :urls.py @Author:张宇 @Date :2020/7/27 16:40 @Desc : '''
from django.urls import path
from .views.base import Index
from .views.auth import Login

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='dashboard_login')
]
