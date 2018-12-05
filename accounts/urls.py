from django.urls import path

from . import views

urlpatterns = [
  path('login', views.login, name='login' ),
  path('register', views.register, name='register' ),
  path('search', views.logout, name='logout' ),
  path('search', views.dashboard, name='dashboard' )
]