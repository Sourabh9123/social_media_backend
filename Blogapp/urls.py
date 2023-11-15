from django.urls import path
from Blogapp.views import BlogviewList, Blogcreate,BlogViewSingle,MyBlogsView, CommentView ,UpdateDeleteComment, CommentReplyView


urlpatterns = [
    path("", BlogviewList.as_view(), name="blog"),
    path('create/',Blogcreate.as_view(), name="create-post"),
    path('single/<str:pk>',BlogViewSingle.as_view(), name="single-post"),
    path('comment/',CommentView.as_view(), name="single-post"),
    path('my-post/',MyBlogsView.as_view(), name="my-post"),
    path('comment/<str:pk>/',UpdateDeleteComment.as_view(), name=""),
    path('comment/reply/',CommentReplyView.as_view(), name=""),

]
