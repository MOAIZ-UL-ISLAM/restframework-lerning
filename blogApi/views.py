from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serilizers import PostSerializer


@api_view(['GET'])
def index(request):
    return Response({"Sucess": "My Api End Point"})


@api_view(['GET'])
def get_all_posts(request):
    get_posts = Post.objects.all()
    serializer = PostSerializer(get_posts, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_post(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Sucess": "Post Created"})
    else:
        return Response(serializer.errors, status=400)


@api_view(["DELETE"])
def delete_post(request):
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({"Sucess": "Post Deleted"})
    except Post.DoesNotExist:
        return Response({"error": "post dosent exist"}, status=404)


@api_view(["GET"])
def get_post(request):
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({"error": "post dose'nt exist"}, status=404)
