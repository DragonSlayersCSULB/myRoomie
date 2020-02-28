from django.contrib import admin
from .models import Post
from .models import Bills

# Register your models here.
admin.site.register(Post) #pass in the post model
admin.site.register(Bills) #pass in the bills model