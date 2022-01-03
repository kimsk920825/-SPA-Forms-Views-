from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from django.contrib.auth import get_user_model

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.tag_set.add(*post.extract_tag_list())
            messages.success(request, "포스팅을 저장했습니다.")
            return redirect("post")
    else:
        form = PostForm()
    return render(request, "instagram/post_form.html", {
        "form" : form,
    })

"""
포스트 작성 후 해당 포스트 화면 -> post_detail
"""
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'instagram/post_detail.html', {
        "post": post
    })
"""
유저가 올린 사진을 모아두는 유저 페이지 view
"""
def user_page(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    post_list = Post.objects.filter(author=page_user)
    post_list_count = post_list.count()
    return render(request, "instagram/user_page.html", {
        "page_user" : page_user,
        "post_list" : post_list,
        "post_list_count" : post_list_count,
    })

"""
default 페이지
"""
def index(request):
    return render(request, "instagram/index.html", {
        
    })