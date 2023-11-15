from django.shortcuts import render

from finddeveloper.models import Profile, Project, Tag, Review
from finddeveloper.serializers import ProfileSerializer,  ProjectSerializer,  ReviewSerializer, TagSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework  import generics




class ProfileView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer





class ProfileSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer




class ProjectView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



class ProjectSingleView( generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer




class ReviewSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



class ReviewView(generics.ListCreateAPIView,  generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer