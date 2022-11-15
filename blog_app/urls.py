from django.urls import path
from .views import BlogView,DetailView
app_name = 'blog_app'

urlpatterns=[
    path('', BlogView, name='blog'),
    path('detail/<slug:post>/',DetailView,name='detail')
]