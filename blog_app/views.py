from django.shortcuts import render

# Create your views here.


def BlogView(request):
    return render(request, 'blog.html')