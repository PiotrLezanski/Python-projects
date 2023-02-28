from django.db import models
from django.contrib.auth.models import User

STATUS = {(0, 'Draft'), (1, 'Publish')}


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    # to - pick User from the list, on_delete - what happens when user is deleted from
    #     the database - CASCADE - all articles are deleted too
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    # in admin panel the name of the Post is viewed
    def _str_(self):
        return self.title

