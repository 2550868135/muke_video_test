''' @File :urls.py @Author:张宇 @Date :2020/7/27 16:40 @Desc : '''
from django.urls import path
from .views.base import Index
from .views.auth import Login, AdminManger,Logout,UpdateAdminStatus
from .views.video import ExternalVideo

urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login/', Login.as_view(), name='login'),
    path('admin/manager/', AdminManger.as_view(), name='admin_manager'),
    path('logout/',Logout.as_view(),name='logout'),
    path('admin/manager/update/status/',UpdateAdminStatus.as_view(),name='admin_update_status'),
    path('video/external/',ExternalVideo.as_view(),name='external_video')
]
