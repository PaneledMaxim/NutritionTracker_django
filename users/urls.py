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
    register_view,
    respond_friend_request_view,
)

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('friends/', friends_list_view, name='friends_list'),
    path('friends/find/', find_friends_view, name='find_friends'),
    path('friends/requests/', friend_requests_view, name='friend_requests'),
    path('friends/add/<int:user_id>/', add_friend_view, name='add_friend'),
    path(
        'friends/requests/<int:request_id>/<str:action>/',
        respond_friend_request_view,
        name='respond_friend_request',
    ),
]
