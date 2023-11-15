from rest_framework.serializers import ModelSerializer
from Blogapp.models import blog, Comments, CommentReplies
from account.serializers import UserSerializer
from rest_framework import serializers
from account.models import  User
from django.contrib.auth import get_user_model
from psycopg2 import errors

User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model =  User
        fields = ['first_name', 'last_name','id']

class blogSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = blog
        fields = ['uuid','content', 'image', 'title', 'user']
    
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        blog_instance = blog.objects.create(
            user=user,
            **validated_data
        )
        return blog_instance
    
    def update(self, instance, validated_data):
        request = self.context.get('request')

        post_owner = request.user
      
        user = instance.user
        # post_owner_obj = User.objects.get(user=post_owner)
        if post_owner == user:
            instance.content = validated_data.get('content', instance.content)
            instance.image = validated_data.get('image', instance.image)
            instance.title = validated_data.get('title', instance.title)
            instance.save()
            return instance
        else:
            return instance
        
    def delete(self, instance):
        request = self.context.get('request')
        post_owner = request.user
        user = instance.user
        # post_owner_obj = User.objects.get(user=post_owner)
        if post_owner == user:
            instance.delete()
        else:
            return  instance
        
class CommentRepliesSerializer(ModelSerializer):
    class Meta:
        model = CommentReplies
        fields = ['comment', 'reply_comment', 'uuid', 'user']


class CommentSerializer(ModelSerializer):
    # reply = CommentRepliesSerializer(read_only=True)
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Comments
        fields = ['user','blog_comment', 'comment', 'id']
        depth = 1

    # def create(self, validated_data):
    #     request = self.context.get('request')
 
    #     user = request.user.id if request else None
     
    #     comments = Comments.objects.create(
    #             user=user,
        
    #             **validated_data
    #         )

    #     return comments
