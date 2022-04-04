from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from saathi.models import Post
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework import viewsets
from rest_framework import permissions


class PostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        is_owner = obj.author == request.user
        if request.method == "DELETE":
            return is_owner or request.user.is_superuser

        return is_owner


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [PostPermission]
    parser_classes = [FormParser, MultiPartParser, JSONParser]

    class PostListSerializer(serializers.ModelSerializer):
        author = serializers.StringRelatedField()
        modified = serializers.DateTimeField(format="%A, %d,%B, %Y")
        class Meta:
            model = Post
            fields = ["id","created", "modified", "author", "image", "title", "body"]

    serializer_class = PostListSerializer
    queryset = Post.objects.all()
