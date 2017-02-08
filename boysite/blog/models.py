from django.db import models
# from django.utils import timezone
# from django.contrib.auth import User



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User')

    # published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
