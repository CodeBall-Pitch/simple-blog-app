from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.site_header='admin Panel'
admin.site.site_title='admin Panel'
admin.site.index_title='admin Panel'


class AuthorAdmin(admin.ModelAdmin):
    list_display=('title','slug','published','status')
    prepopulated_fields={'slug':('title',)}
admin.site.register(Post,AuthorAdmin)
