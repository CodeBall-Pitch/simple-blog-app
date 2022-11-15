from django.shortcuts import render

# Create your views here.

def AccountView(request):
    
    context={}
    return render(request,'accounts/mail.html')