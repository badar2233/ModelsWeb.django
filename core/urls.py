from .views import home,signupview,loginview,dashboardview,blogdetailview,CreateBlogView
from django.urls import path

urlpatterns=[
    path ('', home,name='index.html'),
    path ('signup/',signupview.as_view(), name='signup'),
    path ('login/',loginview.as_view(), name='login'),
    path ('dashboard/',dashboardview.as_view(), name='dashboard'),
    path ('blogdetail/<int:id>',blogdetailview.as_view(), name='blogdetail'),
    path ('createblog', CreateBlogView.as_view(), name='createblog'),



]