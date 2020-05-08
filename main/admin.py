from django.contrib import admin
from .models import Post
from .models import Bill

# Register your models here.
admin.site.register(Post) #pass in the post model
admin.site.register(Bill) #pass in the bills model