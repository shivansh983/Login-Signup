from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            return redirect('login')
    return render(request, 'signup.html')

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('search')
        else:
            error_message = 'Incorrect username or password'
    return render(request, 'login.html', {'error_message': error_message})

@login_required
def search(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        results = User.objects.filter(Q(email__icontains=query) | Q(username__icontains=query))
    return render(request, 'search.html', {'results': results})
