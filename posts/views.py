from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'home.html', context=context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }

    # Check if the post ID is stored in the session
    viewed_posts = request.session.get('viewed_posts', [])

    if post.id not in viewed_posts:
        # Increment view count
        post.views += 1
        post.save()

        # Store the post ID in the session
        viewed_posts.append(post.id)
        request.session['viewed_posts'] = viewed_posts

    return render(request, 'post_detail.html', context=context)


def about(request):
    return render(request, 'about.html')


def blog(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'blog.html', context=context)


def search(request):
    posts = []
    if request.method == 'GET':
        query = request.GET.get('q')
        print(query)

        if query:
            posts = Post.objects.filter(
                Q(title__icontains=query)
            )
        else:
            posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'blog.html', context=context)
