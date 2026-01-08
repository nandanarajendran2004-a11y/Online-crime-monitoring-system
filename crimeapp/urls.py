from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('citizen/register/', views.register_view, name='citizen_register'),
    path('citizen/login/', views.login_view, name='citizen_login'),
    path('citizen/logout/', views.logout_view, name='citizen_logout'),
    path('citizen/report/', views.submit_report, name='submit_report'),
    path('citizen/myreports/', views.my_reports, name='my_reports'),
]
