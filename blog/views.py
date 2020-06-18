from datetime import datetime
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileInfoForm, PostForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post, UserProfileInfo, PostComment
from django.contrib.auth.models import User


def index(request):
    return render(request, 'main/index.html')


def display_posts(request, post_no):
    try:
        post = Post.objects.get(pk=post_no)
        user = User.objects.get(username=post.post_user_id)
        user_profile = UserProfileInfo.objects.get(pk=user.pk)
    except (Post.DoesNotExist, UserProfileInfo.DoesNotExist, User.DoesNotExist):
        raise Http404("Post does not exist!")
    return render(request, 'main/display_post.html', {'post': post,
                                                      'user_profile': user_profile})


def display_comments(request, post_no):
    try:
        post = Post.objects.get(pk=post_no)
        all_comments = PostComment.objects.all().filter(post_id=post).order_by('-date_created')
        post_name = post.post_name
    except PostComment.DoesNotExist or Post.DoesNotExist:
        all_comments = None
        post_no = None
        post_name = None
    return render(request, 'main/all_comments.html', {'all_comments': all_comments,
                                                      'post_id': post_no, 'post_name': post_name})


def delete_comment(request, comment_no):
    if request.user.is_authenticated:
        try:
            comment = PostComment.objects.get(pk=comment_no)
            post = comment.post_id
            user = post.post_user_id
            user_profile = UserProfileInfo.objects.get(pk=user.id)
        except (KeyError, PostComment.DoesNotExist, User.DoesNotExist, UserProfileInfo.DoesNotExist, Post.DoesNotExist):
            return render(request, 'main/index.html', {'error_message': "Comment or post does not exist!", 'error': True})
        else:
            if comment.user_id == request.user:
                comment.delete()
            return render(request, 'main/display_post.html', {'post': post, 'user_profile': user_profile})
    else:
        redirect("blog:enter")


def delete_post(request, post_no):
    if request.user.is_authenticated:
        try:
            post = Post.objects.get(pk=post_no)
        except (KeyError, Post.DoesNotExist):
            return redirect("blog:index", args=({'error_message': "Post does not exist!", 'error': True}))
        else:
            if post.post_user_id.user == request.user:
                post.delete()
            return redirect('blog:my_blogs')
    else:
        return redirect("blog:index")

def edit_post(request, post_no):
    if request.method == 'POST':
        Post.objects.filter(pk=post_no).update(post_name=request.POST.get('title'))
        Post.objects.filter(pk=post_no).update(post_content=request.POST.get('myeditablediv'))
        return redirect("/" + str(post_no))
    else:
        if request.user.is_authenticated:
            post = Post.objects.get(pk=post_no)
            return render(request, 'main/edit_post.html', {'post': post})
        else:
            return redirect('blog:index') 

def enter(request):
    if request.user.is_authenticated:
        return render(request, 'main/index.html')
    else:
        return render(request, 'account/initial.html')


def profile(request):
    if request.user.is_authenticated:
        user_profile = UserProfileInfo.objects.get(pk=request.user.id)
        return render(request, 'account/profile.html', {'user_profile': user_profile})
    else:
        raise Http404("Login first!")


def my_blogs(request):
    if request.user.is_authenticated:
        all_posts = Post.objects.all().order_by('-date_created')
        my_posts = Post.objects.filter(post_user_id=request.user.id).order_by('-date_created')
        return render(request, 'main/my_blogs.html', {'all_posts': all_posts, 'my_posts': my_posts})
    else:
        return redirect("blog:index")


def write_post(request):
    if request.method == 'POST':
        post_form = PostForm({'post_name': request.POST.get('title'),
                              'post_user_id': request.user.pk,
                              'post_content': request.POST.get('myeditablediv')})
        if post_form.is_valid():
            new_post = post_form.save()
            return redirect("/" + str(new_post.pk))
        else:
            return HttpResponse("Invalid Form!")

    else:
        if request.user.is_authenticated:
            return render(request, 'main/write_post.html')
        else:
            return redirect("blog:index")


def write_comment(request, post_no):
    if request.method == 'POST':
        comment_form = CommentForm({'post_id': post_no,
                              'user_id': request.user.pk,
                              'comment': request.POST.get('comment')})
        if comment_form.is_valid():
            new_comment = comment_form.save()
            return redirect("/" + str(post_no))
        else:
            return HttpResponse("Invalid Form!")

    else:
        if request.user.is_authenticated:
            post = Post.objects.get(pk=post_no)
            post_name = post.post_name
            return render(request, 'main/write_comment.html', {'post_name': post_name})
        else:
            redirect("blog:index")


@login_required
def user_logout(request):
    logout(request)
    return redirect("blog:index")


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            user_form_errors = None
            profile_form_errors = None
        else:
            user_form_errors = user_form.errors
            profile_form_errors = profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        user_form_errors = None
        profile_form_errors = None
    return render(request, 'account/registration.html', {'user_form': user_form, 'profile_form': profile_form,
                'registered': registered, 'user_errors': user_form_errors, 'profile_errors': profile_form_errors})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("blog:index")
        else:
            return render(request, 'account/login.html', {'error_message': "Invalid login details given.\nLogin failed."})

    else:
        return render(request, 'account/login.html', {'error_message': None})
