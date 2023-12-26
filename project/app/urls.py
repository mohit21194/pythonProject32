from django.urls import path
from app import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.handleLogin, name='handleLogin'),
    path('logout/', views.handleLogout, name='handleLogout'),

]
