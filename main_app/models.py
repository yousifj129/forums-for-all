from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin" # value saved in db, value shown to the user
        USER = "user", "User"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
        null=True
    )
    
    icon = models.ImageField('Icon', upload_to='images/', default="6522516.png")
    


class Forum(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forums')
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200, default="")

# https://stackoverflow.com/questions/74706092/django-imagefield-with-multiple-images
class Attachment(models.Model):
    class AttachmentType(models.TextChoices):
        PHOTO = "photo", "Photo"
        VIDEO = "video", "Video"

    file = models.ImageField('Attachment', upload_to='images/')
    file_type = models.CharField('File type', choices=AttachmentType.choices, max_length=10)

    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name="attachments")

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)


# https://stackoverflow.com/questions/62879957/how-to-implement-a-like-system-in-django-templates
class Upvote(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='upvotes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvotes')
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'forum'], name="unique_upvote"),
        ]

class Downvote(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='downvotes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downvotes')
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'forum'], name="unique_downvote"),
        ]

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower', 'followed'], name="unique_follow"),
        ]