from django.urls import path 
from . import views


app_name = "users"

urlpatterns = [
    path("login", views.LoginView.as_view(), name = "login"),
    path("login/github", views.github_login, name="github_login"),
    path("login/github/callback", views.github_callback, name="github-callback"),
    path("login/kakao", views.kakao_login, name="kakao_login"),
    path("login/kakao/callback", views.kakao_callback, name="kakao-callback"),
    path("logout", views.log_out, name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),

    ]
