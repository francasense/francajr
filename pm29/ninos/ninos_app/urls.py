from django.urls import path
from .views import home,confirm,account,login,logout,api
urlpatterns = [
    path('',home,name="home"),
    path('account',account,name="account"),
    path('confirm',confirm,name='conf'),
    path('login',login,name='login'),
    path('logout',logout,name="logout"),
    path('api',api,name="api")
]
