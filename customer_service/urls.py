from django.urls import path
from .import views

#

urlpatterns = [
    path('register_support_team/',views.register_support_team,name='register_support_team'),
    path('login_support_team/',views.login_support_team,name='login_support_team'),
    path('manage_requests/', views.manage_requests, name='manage_requests'),
    path('/resolve_request/<int:request_id>/', views.resolve_request, name='resolve_request'),
    path('logout_support_team/', views.logout_support_team, name='logout_support_team'),

   
]
