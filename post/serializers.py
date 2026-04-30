from rest_framework import serializers
from post.models import Post, Project

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError('Title bo‘sh bo‘lmasin')
        return value

    def validate_content(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Content kamida 10 ta belgidan iborat bo‘lsin')
        return value

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "title",
            "description",
            "owner"
        )
