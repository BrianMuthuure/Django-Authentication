from django.urls import path

from accounts.views import home, login_view, register_view

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
]