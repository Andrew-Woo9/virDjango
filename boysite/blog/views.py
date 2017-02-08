from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    post = Post.objects.order_by(Post.created_date)
    context = {
        'post_list': post,
    }

    return render(request, 'blog/post-list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post_detail': post,
    }
    return render(request, 'blog/post-detail.html', context)
