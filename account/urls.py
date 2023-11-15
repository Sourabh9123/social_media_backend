from django.urls import path
from account import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView
)



urlpatterns = [
    path('signup/',views.SignUpView.as_view(), name='signup'),
    path('login/',views.LogInview.as_view(), name='login'),
    path('logout/',views.LogOutView.as_view(), name='logout'),
    path('change-passowrd/',views.PasswordChangeView.as_view(), name='password-change'),
    

    #jwt token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'), # for blacklisting
    
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # for verification
    
]
