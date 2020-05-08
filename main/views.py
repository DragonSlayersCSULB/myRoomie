from django.shortcuts import redirect, render
from .models import Post #from models file in current package
from .models import Bill #from models file in current package
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# def mainLoginScreen(request):
#     context = {
#         # 'posts': posts
#         'login': Post.objects.all()
#     }
#     return render(request, 'main/mainLoginScreen.html', context)

def mainLoginScreen(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        post = User.objects.filter(username = username)
        if post:
            username = request.POST['username']
            request.session['username'] = username
            return redirect("profile")
        else:
            return render(request, 'main/mainLoginScreen.html', {})
    return render(request, 'main/mainLoginScreen.html', {})

def profile(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username = posts)
        return render(request, 'users/profile.html', {"query":query})
    else:
        return render(request, 'main/mainLoginScreen.html', {})

def logout(request):
    try:
        del request.session['username']
    except:
      pass
    return render(request, 'main/mainLoginScreen.html', {})


def home(request):
    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})


def roommates(request):
    context = {
        # 'profiles': profiles
        'profiles': Profile.objects.all()
    }
    return render(request, 'main/roommates.html', context)


def bills(request):
    context = {
        'bills': Bill.objects.all()
    }
    return render(request, 'main/bills.html', context)

def repairs(request):
    return render(request, 'main/repairs.html', {'title': 'Repairs'})

def crowdfund(request):
    return render(request, 'main/crowdfund.html', {'title': 'Crowdfund'})

def calendar(request):
    return render(request, 'main/calendar.html', {'title': 'Calendar'})

def grocery(request):
    return render(request, 'main/grocery.html', {'title': 'Grocery'})

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

class BillCreateView(CreateView):
    model = Bill
    fields = ['title', 'date_posted', 'amount', 'ispaid']
    success_url='/bill'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BillListView(ListView):
    model = Bill
    template_name = 'main/bill.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    #<app>/<model>_<viewtype>.html

class BillDetailView(DetailView):
    model = Bill


class BillUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bill
    fields = ['title', 'date_posted', 'amount', 'ispaid']
    success_url = '/bill' #use this line to return to main page after making an announcement

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class BillDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bill
    success_url='/bill'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False