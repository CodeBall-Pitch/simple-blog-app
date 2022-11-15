from django.urls import path
from .views import BlogView
app_name = 'blog_app'

urlpatterns=[
    path('', BlogView, name='blog')
]