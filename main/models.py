from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() ## unrestricted text because posts can be quite long
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) ## (argument)if user gets deleted, delete their post

    def __str__(self):
        ## dunder str method (double underscore)
        ## these are known as "magic methods"
        return self.title
