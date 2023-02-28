from django.contrib import admin
from .models import Post


# viewing more  data referring to specific post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author')


# Register your models here.
admin.site.register(Post, PostAdmin)







