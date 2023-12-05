from django.shortcuts import render, redirect
from .models import User


# Dummy user data (replace with a database in a real scenario)
users = {
    'Karti': {'password': 'password'},
    'Jaya': {'password': 'pass'},
}


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
            return redirect('success')
        except User.DoesNotExist:
            return redirect('fail')

    return render(request, 'login.html')

def success_view(request):
    return render(request, 'success.html')


def fail_view(request):
    return render(request, 'fail.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            return redirect('fail')
        except User.DoesNotExist:
            User.objects.create(username=username, password=password)
            return redirect('successregister')

    return render(request, 'register.html')
def success_register(request):
    return render(request, 'successregister.html')
