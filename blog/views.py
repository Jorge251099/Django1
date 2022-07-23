from django.shortcuts import render
from django.views.generic import View 
from .forms import PostCreateForm

# Create your views here.
class BlogListView(View):

    def get(self,request,*arg,**kargs):

        context={

        }

        return render(request,'blog_list.html',context)

class BlogCreateView(View):

    def get(self,request,*args,**kargs):
        context={
        }

        return render(request,'blog_create.html',context)

    def Post(self,request,*args,**kargs):
        context={
        }

        return render(request,'blog_create.html',context)
