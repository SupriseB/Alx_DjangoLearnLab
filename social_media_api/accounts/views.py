from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializer
from .models import CustomUser

User = get_user_model()

# -------------------------
# Registration View
# -------------------------
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# -------------------------
# Login View
# -------------------------
class LoginView(generics.GenericAPIView):
    serializer_class = RegisterSerializer  # just for typing; not critical
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

# -------------------------
# Follow a user
# -------------------------
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    if target_user == request.user:
        return Response({'error': "You cannot follow yourself"}, status=400)

    request.user.following.add(target_user)
    return Response({'success': f'You are now following {target_user.username}'}, status=200)

# -------------------------
# Unfollow a user
# -------------------------
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    if target_user == request.user:
        return Response({'error': "You cannot unfollow yourself"}, status=400)

    request.user.following.remove(target_user)
    return Response({'success': f'You have unfollowed {target_user.username}'}, status=200)
