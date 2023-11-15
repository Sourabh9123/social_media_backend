from django.contrib import admin
from Blogapp.models import blog, Comments, CommentReplies



class BlogAdmin(admin.ModelAdmin):
    list_display = ['user',  'image', 'title',"created_at", "updated_at"]
    list_display_links = ['user', 'title']


admin.site.register(blog, BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'blog_comment','comment' ]

admin.site.register(Comments, CommentAdmin)

class CommentRepliesAdmin(admin.ModelAdmin):
    list_display = ['comment' ,'reply_comment', 'uuid']

admin.site.register(CommentReplies, )