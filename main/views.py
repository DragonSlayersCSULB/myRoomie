from django.shortcuts import render
from .models import Post #from models file in current package


# dummy data from the tutorial, ineffective way of doing this
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})
