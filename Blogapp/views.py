from rest_framework import  generics
from account.models import User
from django.contrib.auth import get_user_model

from django.http import Http404
from Blogapp.models import blog, Comments, CommentReplies
from Blogapp.serializers import blogSerializer, CommentSerializer, CommentRepliesSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from rest_framework.permissions import  BasePermission
from rest_framework import permissions
# from Blogapp.permission_class import has_owner
from rest_framework_simplejwt.authentication import JWTAuthentication




User = get_user_model()

class LargeNumberpagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 200
    
  



class BlogviewList(generics.ListAPIView):
    
    queryset = blog.objects.all()
    serializer_class = blogSerializer
    pagination_class = LargeNumberpagination
    filter_backends = [SearchFilter]
    throttle_classes = [UserRateThrottle,AnonRateThrottle]
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'blog_scope_throttle'
    search_fields = ['content', 'title']


# class BlogViewSingle(APIView):
#     def get(self, request, pk):
        
#         try:
#             data = blog.objects.get(pk=pk)
#         except blog.DoesNotExist:
#             raise Http404

#         serializer = blogSerializer(data)
#         return Response(serializer.data,  status=status.HTTP_200_OK)
    
class BlogViewSingle(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [JWTAuthentication]
    
    permission_classes = [IsAuthenticated]

    queryset = blog.objects.all()
    serializer_class = blogSerializer





class Blogcreate(generics.CreateAPIView):
    queryset = blog.objects.all()
    serializer_class = blogSerializer
    permission_classes = [IsAuthenticated]

# class Blogcreate(APIView):
#     def post(self, request, format=None):
#         user  = request.user
#         print(user)
#         user = User.objects.get(id=user.id)
#         data = request.data
#         print(user) 
#         print(data)
#         serializer = blogSerializer(data=data, many=False) 
#         if serializer.is_valid():
#             # serializer.save()
#             return Response(serializer.data,  status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MyBlogsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        blogs = blog.objects.filter(user=user)
        if blogs:
            print(blogs)
            serializer = blogSerializer(blogs, many=True)
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response({"No post":"try to create post first"} , status=status.HTTP_200_OK)



class CommentView(generics.GenericAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

    def get(self, request, *args,  **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):

        data = request.data
        data['user'] = request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    




# class CommentView(generics.ListCreateAPIView):
#     serializer_class = CommentSerializer
#     queryset = Comments.objects.all()



class UpdateDeleteComment(generics.UpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = Comments.objects.get(id=pk)
        data = request.data
        data['user'] = request.user.id
        if data == instance.user:        
            serializer = self.serializer_class(instance=instance, data=data)

            if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    


    
    

class CommentReplyView(generics.ListAPIView):
    queryset = CommentReplies.objects.all()
    serializer_class = CommentRepliesSerializer

    
    def get(self, request, *args,  **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):

        data = request.data
        data['user'] = request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
