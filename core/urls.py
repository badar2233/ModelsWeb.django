from .views import (home,signupview,loginview,dashboardview,blogdetailview,CreateBlogView,EditBlogView,delte_blog,forgetView,verify_otpView,reset_passwordView)
from django.urls import path
# from django.contrib.auth import views as auth_views

urlpatterns=[
    path ('', home,name='index.html'),
    path ('signup/',signupview.as_view(), name='signup'),
    path ('login/',loginview.as_view(), name='login'),
    path ('dashboard/',dashboardview.as_view(), name='dashboard'),
    path ('blogdetail/<int:id>',blogdetailview.as_view(), name='blogdetail'),
    path ('createblog', CreateBlogView.as_view(), name='createblog'),
    path ('updateblog/<int:id>', EditBlogView.as_view(),name='updateblog'),
    path ('deleteblog/<int:id>',delte_blog,name='deleteblog'),
    path ('forget/',forgetView.as_view(),name='forget'),
    path ('verify_otp/',verify_otpView.as_view(),name='verify_otp'),
    path ('reset_password/<int:id>',reset_passwordView.as_view(),name='reset_password'),





]