from rest_framework import viewsets, permissions, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# -------------------------
# Permissions: Only allow owners to edit/delete
# -------------------------
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

# -------------------------
# Pagination for posts/comments
# -------------------------
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

# -------------------------
# Post CRUD
# -------------------------
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# -------------------------
# Comment CRUD
# -------------------------
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# -------------------------
# Feed: Posts from followed users
# -------------------------
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

# -------------------------
# Like a post
# -------------------------
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    if user in post.likes.all():
        return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
    post.likes.add(user)
    return Response({'success': f'Post "{post.title}" liked.'}, status=status.HTTP_200_OK)

# -------------------------
# Unlike a post
# -------------------------
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    if user not in post.likes.all():
        return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
    post.likes.remove(user)
    return Response({'success': f'Post "{post.title}" unliked.'}, status=status.HTTP_200_OK)
