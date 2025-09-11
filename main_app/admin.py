from django.contrib import admin
from .models import Forum, Upvote, Downvote, Comment,User, Attachment, Follow
# Register your models here.
admin.site.register(Forum)
admin.site.register(Upvote)
admin.site.register(Downvote)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Attachment)
admin.site.register(Follow)