from django.shortcuts import get_object_or_404, render

from blog.models import Post

# Create your views here.


def post_list(request):
    posts = Post.published.all()
    return render(request, "blog/post/list.html", {"posts": posts})


# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id, status=Post.status.PUBLISHED)
#     return render(request, "blog/post/detail.html", {"post": post})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.html", {"post": post})
