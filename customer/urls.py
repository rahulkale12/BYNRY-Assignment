from django.urls import path
from .import views
# app_name = 'customer'

urlpatterns = [

    path('', views.register_customer, name='register_customer'),
    path('login_customer/', views.login_customer, name='login_customer'),
    path('logout_customer/', views.logout_customer, name='logout_customer'),
    path('submit_request/', views.submit_service_request, name='submit_request'),
    path('track_request/', views.track_request, name='track_request'),
    path('view_account/', views.view_account, name='view_account'),
]
