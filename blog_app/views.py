from django.shortcuts import render,get_list_or_404
from .models import Post
# Create your views here.


def BlogView(request):
    post=Post.newmanager.all()
    context={
       'post':post
    }
    return render(request, 'blog_app/blog.html',context)
 
def DetailView(request,post):
   post=get_list_or_404(Post,slug=post,status='published')
   
   context={
   'post':post
   }
   return render(request ,'blog_app/detail.html',context)
 
 