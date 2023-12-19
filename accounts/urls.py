from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('password_reset/', auth_views.LogoutView.as_view(template_name="password_reset.html"), name='password_reset'),
    
    # path('signup/', views.SignUpView.as_view(),
    #     name='signup'),
    # path('signup_success/', views.SignUpSuccessView.as_view(),
    #     name='signup_success'),



]
