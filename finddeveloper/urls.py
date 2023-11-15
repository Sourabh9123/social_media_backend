from django.urls import path
from finddeveloper.views import TagView, ReviewView, ProfileView,ProjectView, ReviewSingleView, ProfileSingleView,ProjectSingleView


urlpatterns = [
    path('',ProfileView.as_view(), name='profile' ),
    path('<str:pk>',ProfileSingleView.as_view(), name='profile' ),
    

    
    path('project/<str:pk>',ProjectSingleView.as_view(), name='' ),
    path('project/',ProjectView.as_view(), name='' ),
    
    path('review/',ReviewView.as_view(), name='' ),
    path('review/<str:pk>',ReviewSingleView.as_view(), name='' ),
    path('tags/',TagView.as_view(), name='' ),

]

