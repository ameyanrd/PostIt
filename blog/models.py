from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    about_user = models.CharField(max_length=200)
    age = models.IntegerField()

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_description = models.CharField(max_length=200)

class Post(models.Model):
    post_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_upvotes = models.IntegerField(default=0)
    Post_location = models.CharField(max_length=100)
    
    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['Post_location'], name='unique_location')
                ]

class Post_Tag(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Post_comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)
