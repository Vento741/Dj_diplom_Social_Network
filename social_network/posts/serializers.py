from rest_framework import serializers
from .models import Post, Comment, Like, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image']


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Comment
        fields = ['author', 'text', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True) 
    comments = CommentSerializer(many=True, read_only=True)
    images = PostImageSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    location_name = serializers.CharField(required=False, allow_blank=True)
    latitude = serializers.FloatField(required=False, allow_null=True)
    longitude = serializers.FloatField(required=False, allow_null=True)

    class Meta:
        model = Post
        fields = ['id', 'text', 'created_at', 'images', 'comments', 'likes_count', 'location_name', 'latitude', 'longitude']
        extra_kwargs = {
            'text': {'required': True},
            'images': {'required': False},  # Допустимо, если изображения могут быть опущены
        }

    def get_likes_count(self, obj):
        return obj.likes.count()
