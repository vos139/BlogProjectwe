from django.utils import timezone
from .models import Post, Lear_Post
from .decorators import consultant_required, learner_required
#from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
#from django.urls import reverse_lazy
#from django.utils.decorators import method_decorator
#from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostForm, LearnPostForm, Reply_Form, Learn_Form

#redirection to forum home page
@login_required
def blog_home(request):
    return render(request, 'blog/blog_home.html')

#redirection to knowledge base
@login_required
def links(request):
    return render(request, 'blog/usefull_links.html')


#Consultant add new post, edit post, view list, view posts start from here
@login_required
@consultant_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
@consultant_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
@consultant_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})


@login_required
@consultant_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
@consultant_required
def add_reply(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = Reply_Form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.published_date = timezone.now()
            comment.post=post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Reply_Form(instance=Post)
    return render(request, 'blog/post_reply.html', {'form': form})

@login_required
@consultant_required
def view_reply(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/view_reply.html', {'post': post})


#Learner add new post, edit post, view list, view posts start from here

@login_required
#@learner_required
def learn_post_list(request):
    posts = Lear_Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/learn_post_list.html', {'posts': posts})

@login_required
#@learner_required
def learn_post_detail(request, pk):
    post = get_object_or_404(Lear_Post, pk=pk)
    return render(request, 'blog/learn_post_detail.html', {'post': post})

@login_required
@learner_required
def learn_post_new(request):
    if request.method == "POST":
        form = LearnPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('learn_post_detail', pk=post.pk)
    else:
        form = LearnPostForm()
    return render(request, 'blog/learn_post_edit.html', {'form': form})

@login_required
@learner_required
def learn_post_edit(request, pk):
    post = get_object_or_404(Lear_Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('learn_post_detail', pk=post.pk)
    else:
        form = LearnPostForm(instance=post)
    return render(request, 'blog/learn_post_edit.html', {'form': form})


@login_required
def learn_add_reply(request, pk):
    post = get_object_or_404(Lear_Post, pk=pk)
    if request.method == 'POST':
        form = Learn_Form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.published_date = timezone.now()
            comment.post=post
            comment.save()
            return redirect('learn_post_detail', pk=post.pk)
    else:
        form = Learn_Form(instance=Post)
    return render(request, 'blog/learn_reply.html', {'form':form})




@login_required
def view_learn(request, pk):
    post = get_object_or_404(Lear_Post, pk=pk)
    return render(request, 'blog/view_learn.html', {'post':post})
