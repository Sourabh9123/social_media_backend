from django.contrib import admin
from finddeveloper.models import Profile, Project, Tag, Review



class ReviewAdmin(admin.ModelAdmin):
    list_display = ['profile','project', 'id',"vote", 'created_at','updated_at']
    list_display_links = ['profile', 'project', 'vote']
    search_fields = ['tag']


admin.site.register(Review, ReviewAdmin)









class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'id', 'created_at','updated_at']
    list_display_links = ['id', 'tag']
    search_fields = ['tag']


admin.site.register(Tag, TagAdmin)













class ProjectAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title',  'image','id','created_at','updated_at']
    list_display_links = ['owner', 'title', 'id']
    search_fields = ['owner','title']


admin.site.register(Project, ProjectAdmin)




class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name',"short_intro"  ,'bio', 'image', 'id','created_at','updated_at']
    list_display_links = ['user', 'name', 'id']
    search_fields = ['user','name']


admin.site.register(Profile, ProfileAdmin)


