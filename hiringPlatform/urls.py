from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('user_roles', views.user_roles, name='user_roles'),
    path('job_match', views.available_job, name='job_match'),
    path('logoutPage', views.logoutPage, name='logoutPage'),
    path('demo', views.demoPage, name='demo')

]
