from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# this communicates directly with the database and creates the necessary tables and attributes for us

class Post(models.Model):
    # announcements posts
    title = models.CharField(max_length=100)
    content = models.TextField() ## unrestricted text because posts can be quite long
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) ## (argument)if user gets deleted, delete their post

    def __str__(self):
        ## dunder str method (double underscore)
        ## these are known as "magic methods"
        return self.title


class Bill(models.Model):
    # billing and payments page
    # making changes to this page requires migrations to the database!
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    ispaid = models.BooleanField(default=False)
    #date_due = models.DateField()
    #bills_total = models.Sum()

    def __str__(self):
        ## dunder str method (double underscore)
        ## these are known as "magic methods"

        #cast the decimal value to a string to return
        return self.title
