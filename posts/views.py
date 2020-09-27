from django.shortcuts import render
from rest_framework import generics

from .models import Post
from . serializer import PostSerializer
# Create your views here.

class PostsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

