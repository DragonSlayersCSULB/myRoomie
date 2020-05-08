from django.shortcuts import render, redirect
from .models import Bills
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
# class BillCreateView(CreateView):
#     model = Bills
#     fields = ['title', 'type', 'due-date', 'amount',]


# class BillListView(ListView):
#     model = Bills
#     template_name = 'main/bills.html'
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     #<app>/<model>_<viewtype>.html

# class BillDetailView(DetailView):
#     model = Bills

# class BillCreateView(LoginRequiredMixin, CreateView):
#     model = Bills
#     fields = ['title','content']
#     success_url = '/' #use this line to return to main page after making an announcement

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

# class BillUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Bills
#     fields = ['title','content']
#     success_url = '/' #use this line to return to main page after making an announcement

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False

# class BillDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Bills
#     success_url='/'
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


