from django.urls import path, include
from . import views as user_views
from django.contrib.auth import views as auth_views

from .views import verify_email_message, verify_email_complete, request_new_link, verify_link_expired, new_email_sent

urlpatterns = [
    path('', user_views.index, name='index'),
    path('login/', user_views.login_user, name='login'),
    path('logout/', user_views.logout_user, name='logout'),
    path('register/', user_views.register, name='register'),

    # RESET PASSWORD
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='user_auth/password_reset/password_reset.html',
                                                                 html_email_template_name=
                                                                 'user_auth/password_reset/password_reset_email.html'),name='reset_password'),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='user_auth/password_reset/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='user_auth/password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/password-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='user_auth/password_reset/password_reset_complete.html'), name='password_reset_complete'),

    # EMAIL VERIFICATION

    path('verification/', include('verify_email.urls')),
    path('verification/user/verify-email/request-new-link/', request_new_link, name='request-new-link'),
    path('verify-email-message/', verify_email_message, name='verify_email_message'),
    path('verify-verify-complete/', verify_email_complete, name='verify_email_complete'),
    path('verify-link-expired/', verify_link_expired, name='verify_link_expired'),
    path('new-email-sent/', new_email_sent, name='new_email_sent'),







]