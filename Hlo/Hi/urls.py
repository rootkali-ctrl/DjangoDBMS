# urls.py
from django.urls import path
from .views import login_view, success_view, fail_view, register_view, success_register

urlpatterns = [
    path('', login_view, name='login'),
    path('success/', success_view, name='success'),
    path('fail/', fail_view, name='fail'),
    path('register/', register_view, name='register'),
    path('successregister/', success_register, name='successregister'),
]
