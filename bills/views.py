from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def newBill(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Roommate created for {username}!') #show that the request was successful!
            return redirect('main-home')
    else:
        form = UserRegisterForm() #instantiates an empty form
    return render(request, 'bills/newbill.html', {'form' : form})
