from django.shortcuts import render
from .models import Post #from models file in current package
from users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

class PostListView(ListView):
    model = Post
    template_name = 'main/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    #<app>/<model>_<viewtype>.html

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    success_url = '/' #use this line to return to main page after making an announcement

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    success_url = '/' #use this line to return to main page after making an announcement

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url='/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})

def roommates(request):
    context = {
        # 'posts': posts
        'profiles': Profile.objects.all()
    }
    return render(request, 'main/roommates.html', context)