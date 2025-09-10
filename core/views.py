from django.shortcuts import render,redirect
from django.views import View
from .models import Blog,User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login

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