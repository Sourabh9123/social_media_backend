from django.db import models
import uuid
from account.models import User
from django.contrib.auth import  get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='developer/profile/image', default='developer/project/image/pexels-photo-4622893_3ulZXIM.webp')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE) 
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='developer/project/image', default='developer/project/image/pexels-photo-4622893_3ulZXIM.webp')
    tags = models.ManyToManyField('Tag')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title} by {self.owner.name}"
    

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag
    




class Review(models.Model):
    VOTE_ = (
        ('up','Up-Vote'),
        ('dowm','Down-Vote')

    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    vote = models.CharField(max_length=100, choices=VOTE_ )
    description = models.TextField(null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.project.title

