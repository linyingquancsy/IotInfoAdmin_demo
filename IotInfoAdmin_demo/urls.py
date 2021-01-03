"""IotInfoAdmin_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
import login.views as login_views
import data.views as data_views
from rest_framework.routers import DefaultRouter
from api.views import SenViewSet
# 使用自动URL路由连接我们的API
router = DefaultRouter()
router.register(r'sen', SenViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', login_views.login),
    path('login/', login_views.login),
    path('register/', login_views.register),
    path('logout/', login_views.logout),
    path('confirm/', login_views.user_confirm),
    path('captcha/', include('captcha.urls')),

    path('index/', data_views.index),
    path('User/', data_views.Userv),
    path('Device/', data_views.Device),
    # path('monitoring/', data_views.monitoring),
    path('testing/', data_views.testing),
    # path('setdata/', data_views.set_data.as_view()),

    path('api/', include(router.urls)),
]

