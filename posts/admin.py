from django.contrib import admin

from .models import Category, Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)

admin.site.site_name = 'Custom Commands admin'
admin.site.site_title = 'Custom Commands'
