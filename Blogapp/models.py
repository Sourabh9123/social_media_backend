from django.db import models
from account.models import User
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()



class blog(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_set_obj')
    title = models.CharField(max_length=500)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    image = models.ImageField(upload_to='Blog/images/', default='Blog/images//pexels-photo-4622893-1.webp')

    def __str__(self):
        return f"{self.title} By {self.user.first_name}"
    
    class Meta:
        ordering = ("-created_at",)
    

class Comments(models.Model):
    blog_comment = models.ForeignKey(blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    
    class Meta:
        unique_together = [['blog_comment', 'user'],]
        ordering = ('-created_at','updated_at','comment')

    def __str__(self):
        return f"{self.comment} - by -  {self.blog_comment.uuid}"
    


class CommentReplies(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.DO_NOTHING)
    reply_comment = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    self_reply = models.ForeignKey('self', on_delete=models.DO_NOTHING,  null=True, blank=True)

    
    def __str__(self):
        return f"{self.uuid} - Main Comment Id Is -- {self.comment.id}"