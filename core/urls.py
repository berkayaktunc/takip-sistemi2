from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('izin-talepleri/', views.izin_talepleri, name='izin_talepleri'),
    path('create-leave-request/', views.create_leave_request, name='create_leave_request'),
    path('izin-talepleri/durum-guncelle/<int:request_id>/<str:new_status>/', views.update_status, name='update_status'),
]