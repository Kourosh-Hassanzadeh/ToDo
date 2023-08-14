"""
URL configuration for ToDo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import home
from todoList.views import todo_list, add_todo, update_todo, delete_todo, user_todo_list
from users.views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', todo_list, name='todo_list'),
    path('todo/<str:username>/', user_todo_list, name='user_todo_list'),
    path('add_todo/', add_todo, name='add_todo'),
    path('update_todo/<int:id>/', update_todo, name="update_todo"),
    path('delete_todo/<int:id>/', delete_todo, name="delete_todo"),
    path('register/', register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]
