from .models import FriendRequest


def incoming_friend_requests_count(request):
    if not request.user.is_authenticated:
        return {'incoming_friend_requests_count': 0}

    count = FriendRequest.objects.filter(
        to_user=request.user,
        status=FriendRequest.STATUS_PENDING,
    ).count()
    return {'incoming_friend_requests_count': count}
