from django.shortcuts import render,redirect
from django.views import View
from .models import Blog

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
        print(username,gmail,password)

        if username and gmail and password:
            if username=='badar' and gmail=='badar@gmail' and password=='badar123':
                return redirect('login')
            else:
                return render(request,'signup.html', {'error':'invalid ceredetail'})    
        # print(request.POST)
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
            if username=='badar' and password=='badar123':
                # messages.sucess(request,'Login sucessfull')
                # return redirect('login')
                return redirect('dashboard')
            else:
                return render(request,'login.html', {'error':'invalid ceredetail'})

        # messages.error(request,'invaid')
        # return render(request,'login.html')
        return redirect('dashboard')
    # def login_sucess(request):
    #     # return redirect('dashboard')

class dashboardview(View):
    def get(self,request):
       
        blogs=Blog.objects.all()
        print(blogs)
        context={
            'blogs': blogs
        }
        return render(request,'dashboard.html',context)


# class BlogView(View):
#     def get(self,request):
        

#         return render(request,'blog.html')




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
        blog_image = request.FILES.get('image')

        print (title,1111111111111111111)
        print (content,2222222222222222222)
        print(blog_image,3333333333333333333)


        Blog.objects.create(
            title=title,
            content=content,
            blog_image=blog_image,
        )
        return redirect('dashboard')
        return render(request,'create_blog.html')


