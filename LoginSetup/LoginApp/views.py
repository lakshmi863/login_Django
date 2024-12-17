from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def home(request):
    return render(request, "home.html", {})

def signup(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():  
            form.save()  
            return redirect('login')  
    else:
        form = UserRegisterForm()  

  
    return render(request, 'signup.html', {'form': form})
def login(request):
    return render(request, 'login.html') 