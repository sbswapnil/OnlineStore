from django.urls import path, include
from django.contrib import auth
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('forgot', views.forgotpass, name='forgot'),
    path('logout', views.logout, name='logout'),

    # path('^', include('django.contrib.auth.urls')),

]