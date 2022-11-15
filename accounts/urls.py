from django.urls import path
from .views import AccountView
app_name="accounts"

urlpatterns=[
    path('',AccountView,name='mail')
]