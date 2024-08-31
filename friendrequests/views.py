from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import FriendRequest
from .serializers import FriendRequestSerializer,UserSerializer
from profiles.models import User



class FriendRequestCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Create a friend request, setting the sender as the logged-in user.
        """
        serializer = FriendRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user, status="pending")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AllUsersExceptMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the logged-in user
        user = request.user

        # Retrieve all users except the logged-in user
        users = User.objects.exclude(id=user.id)

        # Serialize the user data
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class FriendRequestALL(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve the logged-in user
        user = request.user

        # Retrieve optional sender_id or receiver_id from query parameters
        sender_id = request.query_params.get('sender_id', None)
        receiver_id = request.query_params.get('receiver_id', None)

        # Build a query to filter FriendRequests where the logged-in user is either the sender or receiver
        if sender_id:
            # Filter friend requests where the user is the sender (or receiver if they match sender_id)
            friend_requests = FriendRequest.objects.filter(sender_id=sender_id)
        elif receiver_id:
            # Filter friend requests where the user is the receiver (or sender if they match receiver_id)
            friend_requests = FriendRequest.objects.filter(receiver_id=receiver_id)
        else:
            # Filter friend requests where the logged-in user is either the sender or receiver
            friend_requests = FriendRequest.objects.filter(sender=user).union(
                FriendRequest.objects.filter(receiver=user)
            )

        # Check if requests exist and serialize the data
        if friend_requests.exists():
            serializer = FriendRequestSerializer(friend_requests, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "No requests found"}, status=status.HTTP_404_NOT_FOUND)
class FriendRequestApproveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        """
        Approve a friend request, setting status to 'accepted'.
        Only the receiver can approve the request.
        """
        friend_request = get_object_or_404(FriendRequest, pk=pk)

        if friend_request.receiver != request.user:
            return Response({'error': 'You do not have permission to approve this request.'},
                            status=status.HTTP_403_FORBIDDEN)

        friend_request.status = "accepted"
        friend_request.save()

        return Response({'status': 'Friend request accepted'}, status=status.HTTP_200_OK)

class FriendRequestRejectView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        """
        Reject a friend request, setting status to 'rejected'.
        Only the receiver can reject the request.
        """
        friend_request = get_object_or_404(FriendRequest, pk=pk)

        if friend_request.receiver != request.user:
            return Response({'error': 'You do not have permission to reject this request.'},
                            status=status.HTTP_403_FORBIDDEN)

        friend_request.status = "rejected"
        friend_request.save()

        return Response({'status': 'Friend request rejected'}, status=status.HTTP_200_OK)

class FriendRequestDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """
        Delete a friend request.
        Only the sender or receiver can delete the request.
        """
        friend_request = get_object_or_404(FriendRequest, pk=pk)

        if friend_request.sender != request.user and friend_request.receiver != request.user:
            return Response({'error': 'You do not have permission to delete this request.'},
                            status=status.HTTP_403_FORBIDDEN)

        friend_request.delete()
        return Response({'status': 'Friend request deleted'}, status=status.HTTP_204_NO_CONTENT)
