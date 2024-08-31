from django.urls import path
from .views import FriendRequestCreateView, FriendRequestApproveView, FriendRequestRejectView, FriendRequestDeleteView, FriendRequestALL,AllUsersExceptMeView

urlpatterns = [
    path('create/', FriendRequestCreateView.as_view(), name='friend-request-create'),
    path('viewrequests/',FriendRequestALL.as_view(), name='friend-request-all'),
    path('allProfiles/',AllUsersExceptMeView.as_view(), name='profiles-all'),

    path('<int:pk>/approve/', FriendRequestApproveView.as_view(), name='friend-request-approve'),
    path('<int:pk>/reject/', FriendRequestRejectView.as_view(), name='friend-request-reject'),
    path('<int:pk>/delete/', FriendRequestDeleteView.as_view(), name='friend-request-delete'),
]
