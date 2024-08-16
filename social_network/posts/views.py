from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment, Like, PostImage
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied


# ViewSet для постов
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    # переопределяем метод create для сохранения изображений
    def perform_create(self, serializer):
        post = serializer.save(author=self.request.user)
        images = self.request.FILES.getlist('images')
        for image in images:
            PostImage.objects.create(post=post, image=image)

    # переопределяем метод update для проверки авторства
    def perform_update(self, serializer):
        post = serializer.instance
        if post.author != self.request.user:
            raise PermissionDenied("Вы не можете редактировать эту публикацию.")
        serializer.save()

    # переопределяем метод destroy для проверки авторства
    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("Вы не можете удалять эту публикацию.")
        instance.delete()


    # def create(self, request, *args, **kwargs):
    #     files = request.FILES
    #     if 'images' in files:
    #         images = files.getlist('images')
    #         request.data._mutable = True
    #         request.data['images'] = images
    #         request.data._mutable = False
    #     return super().create(request, *args, **kwargs)

# ViewSet для комментариев
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        return post.comments.all()

# ViewSet для лайков
class LikeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['post_pk'])
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            like.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
        return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)

