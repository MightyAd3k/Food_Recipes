from django.urls import path
from accounts import views
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("user_profile/", views.user_profile, name="user_profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("change_password/", views.change_password, name="change_password"),
    # path("change_password_done/", views.change_password_done, name="change_password_done"),
    path("password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path("password_reset_done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("password_reset_complete/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout")
]
