from django.urls import path
from apps.authentication import views
from apps.authentication import controller_logic

urlpatterns = [
    path('', views.otp_login, name='home'),
    path('register/', views.register, name='register'),
    path('otp_validate/', views.otp_validate, name='otp_validate'),
    path("logout/", views.logout_view, name="logout"),
    
    path("send_otp/", controller_logic.mobial_otp_logic, name="send_otp"),
    path("validate_otp/", controller_logic.mobial_otp_verify_logic, name="validate_otp"),
    path('user_register/', controller_logic.user_register, name='user_register'),

]
    
