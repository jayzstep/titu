from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms 
from datetime import datetime
from django.utils import timezone

# Create your views here.
#@login_required(login_url="/users/login/")
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})

#@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            # current_date = timezone.localtime(timezone.now())
            # post_amount_today = Post.objects.filter(author=request.user, date__date=current_date).count()
            # if post_amount_today > 10:
            #     return HttpResponse("Error, too many messages sent today")
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', {'form': form})
