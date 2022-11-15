from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    class NewManger(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    Options=(
        ('draft','Draft'),
        ('published','Published'),
    )
    title=models.CharField(max_length=100,blank=True,null=True)
    slug=models.SlugField(max_length=100,unique=True,blank=True,null=True)
    published=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    content=models.TextField(max_length=1000,blank=True,null=True)
    status=models.CharField(max_length=10,choices=Options,default='draft',blank=True,null=True)
    objects=models.Manager()
    newmanager=NewManger()
    
    
    class Meta:
        ordering=('-published',)
    def __str__(self):
        return self.title