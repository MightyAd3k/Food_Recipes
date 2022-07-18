from django.urls import path
from accounts import views


urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("user_profile/", views.user_profile, name="user_profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("change_password/", views.change_password, name="change_password"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout")
]
