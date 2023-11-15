from rest_framework.serializers import ModelSerializer
from finddeveloper.models import Profile, Project, Tag, Review
from account.serializers import UserSerializer




class ProfileSerializer(ModelSerializer):
    user = UserSerializer
    class Meta:
        model = Profile
        fields = "__all__"
        depth = 1




class ProjectSerializer(ModelSerializer):
    profile = ProfileSerializer
    class Meta:
        model = Project
        fields = "__all__"
        depth =1


class ReviewSerializer(ModelSerializer):
    profile = ProfileSerializer
    project = ProjectSerializer
    class Meta:
        model = Review
        fields = "__all__"
        depth = 1


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"



