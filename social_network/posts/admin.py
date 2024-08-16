from django.contrib import admin

# Register your models here.

from .models import Post, PostImage, Comment, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at', 'author')
    search_fields = ('text', 'author__username')
    list_filter = ('created_at', 'author')

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    search_fields = ('image',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at', 'author', 'post')
    search_fields = ('text', 'author__username', 'post__text')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user')
    search_fields = ('post__text', 'user__username')
