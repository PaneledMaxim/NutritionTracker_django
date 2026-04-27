from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    add_friend_view,
    edit_profile_view,
    find_friends_view,
    friend_requests_view,
    friends_list_view,
    home_view,
    login_view,
    logout_view,
    profile_view,
    remove_friend_view,
    register_view,
    respond_friend_request_view,
    user_profile_view,
)

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html',
            email_template_name='registration/password_reset_email.html',
            subject_template_name='registration/password_reset_subject.txt',
            success_url='/password-reset/done/',
        ),
        name='password_reset',
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html',
            success_url='/reset/done/',
        ),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('users/<str:username>/', user_profile_view, name='user_profile'),
    path('friends/', friends_list_view, name='friends_list'),
    path('friends/find/', find_friends_view, name='find_friends'),
    path('friends/requests/', friend_requests_view, name='friend_requests'),
    path('friends/add/<int:user_id>/', add_friend_view, name='add_friend'),
    path('friends/remove/<int:user_id>/', remove_friend_view, name='remove_friend'),
    path(
        'friends/requests/<int:request_id>/<str:action>/',
        respond_friend_request_view,
        name='respond_friend_request',
    ),
]
