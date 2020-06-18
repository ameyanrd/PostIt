from django import forms
from .models import UserProfileInfo, Post, PostComment
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password')


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('name', 'about', 'age', 'email')


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = "__all__"


class CommentForm(forms.ModelForm):

    class Meta():
        model = PostComment
        fields = "__all__"
