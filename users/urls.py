# users/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]