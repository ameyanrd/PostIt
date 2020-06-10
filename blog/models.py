from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    about = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_description = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    post_name = models.CharField(max_length=100)
    post_user_id = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
    date_created = models.CharField(max_length=100)
    # post_location = models.CharField(max_length=100)
    post_content = models.TextField(max_length=5000)
    '''
    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['post_location'], name='unique_location')
                ]
    '''

    def __str__(self):
        return self.post_name


class PostTag(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)


class PostComment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)
    date_created = models.DateField()

    def __str__(self):
        return self.comment
