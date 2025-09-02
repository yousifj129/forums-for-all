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
        # default=Role.CUSTOMER,
        null=True
    )


class Forum():
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forums')
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)
# https://stackoverflow.com/questions/74706092/django-imagefield-with-multiple-images
class Attachment():
    class AttachmentType(models.TextChoices):
        PHOTO = "Photo", _("Photo")
        VIDEO = "Video", _("Video")

    file = models.ImageField('Attachment', upload_to='attachments/')
    file_type = models.CharField('File type', choices=AttachmentType.choices, max_length=10)

    publication = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name="attachments")

    class Meta:
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'
class Comment():
    commenter = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=1000)

# https://stackoverflow.com/questions/62879957/how-to-implement-a-like-system-in-django-templates
class Upvote():
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='upvotes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvotes')
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name="unique_upvote"),
        ]

class Downvote():
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='downvotes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downvotes')
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name="unique_downvote"),
        ]
