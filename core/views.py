from django.shortcuts import render,redirect
from django.views import View
from .models import Blog,User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login
import random
from django.core.mail import send_mail

#shw blogs to respective users
#Give assess to 

# Create your views here.
def home(request):
    name="badar"
    context={'name':name,
    'email':'badar@gmail.com',
    'age':18}
    return render(request,'index.html', context)

class signupview(View):
    def get (self,request):
        return render(request, 'signup.html')

    def post(self,request):
        username=request.POST.get('username')
        gmail=request.POST.get('gmail')
        password=request.POST.get('password')
        first_name=request.POST.get('firstname')
        print(username,gmail,password)

        if username and gmail and password:
            user = User.objects.create(
                username=username,
                email=gmail,
                first_name=first_name,
            )
            passwordssss = make_password(password)
            user.password = passwordssss
            user.save()
            return redirect('login')
        #     else:
        #         return render(request,'signup.html', {'error':'invalid ceredetail'})    
        # # print(request.POST)
        # print("simple query")
        # return redirect('login')
        # return render(request,'signup.html',{'message': 'Signup sucessful'})
        # messages.error(request, 'try again')
        return render (request,'signup.html')

class loginview(View):
    def get (self,request):
        return render(request, 'login.html')

    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)

        if username and password:
            user= User.objects.filter(username=username).first()
            print(check_password(password,user.password))
            if user and check_password(password,user.password):
                print(user)
                login(request, user)
            
                return redirect('dashboard')
            
        return redirect('login')
   
class dashboardview(View):
    def get(self,request):
       
        blogs=Blog.objects.all()
        print(blogs)
        context={
            'blogs': blogs
        }
        return render(request,'dashboard.html',context)







class blogdetailview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        print(id)

        blog=Blog.objects.filter(id=id).first()
        
        context = {
            'blog': blog
          }
        return render(request,'blogdetail.html',context)



class CreateBlogView(View):
    def get(self,request):
        return render(request,'create_blog.html')

    def post(self,request):
        print("simple query")
        print(request.POST)
        title = request.POST.get('title')
        content = request.POST.get('content')
        blog_image = request.FILES.get('blog_image')

        print (title,1111111111111111111)
        print (content,2222222222222222222)
        print(blog_image,3333333333333333333)

       
        Blog.objects.create(
            title=title,
            content=content,
            blog_image=blog_image,
            author = request.user,
        )
        return redirect('dashboard')
        # return render(request,'create_blog.html')



class EditBlogView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        

        blog=Blog.objects.filter(id=id).first()
        
        context = {
            'blog': blog
          }
        return render(request,'editblog.html',context)
    def post(self,request,*args,**kwargs):
        id= kwargs.get('id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        blog_image = request.FILES.get('image')

        blog = Blog.objects.filter(id=id).first()
        blog.title= title
        blogcontent= content
        if blog_image:
            blog.blog_image=blog_image
            blog.save()

        return redirect('dashboard')

def delte_blog(request,*args,**kwargs):
    id = kwargs.get('id')
    blog = Blog.objects.filter(id=id).first()
    if blog:
        blog.delete()
    return redirect('dashboard')



class forgetView(View):
    def get (self,request,*args,**kwargs):
        return render(request, 'forget.html')
  
    def post(self,request,*args,**kwargs):
        email=request.POST.get('gmail')
        print(email,"gmail")
        if email:
            user=User.objects.filter(email=email).first()
            print(User)
        if User:
            print(User)
            opt = random.randint(10000,99999)
            message = f"Otp for your forget password is {opt}"
            send_mail(
                "Forget Password Email",
                message,
                "Star@college",
                [email]
            )
            user.otp = opt
            user.save()
            print(opt)
            return redirect('verify_otp')

        return render(request,'forget.html')
class verify_otpView(View):
    def get (self,request,*args,**kwargs):
        return render(request, 'verify_otp.html')

    def post(self,request,*args,**kwargs):
        verify_otp = request.POST.get('verify_otp')
        print('ddsfss', verify_otp)
        user= User.objects.filter(otp=verify_otp).first()
        print('gddfsg', user)
        if user:
            user.otp = ""
            user.save()
            print('otp')
            return redirect('reset_password', user.id)
        
        
        return render(request,'verify_otp.html')

class reset_passwordView(View):
    def get (self,request,*args,**kwargs):
        id= kwargs.get("id")
        return render(request, 'reset_password.html', {'id':id})

    def post(self,request,*args,**kwargs):
        password = request.POST.get('password')
        conf_password= request.POST.get('confirm_password') 
        id = kwargs.get("id")
        if password == conf_password:
            user = User.objects.filter(id=id).first()

            user.password = make_password(password)
            user.save()
            return redirect('login')
  