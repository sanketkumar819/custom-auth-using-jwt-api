from django.urls import path,include
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView, TokenVerifyView
from customaccount.views import UserRegistrationView,UserPasswordResetView, UserLoginView,ProfileView,UserChangePasswordView,PasswordResetEmailView

urlpatterns = [
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('passwordresetemail/', PasswordResetEmailView.as_view(), name='passwordresetemail'),
    path('passwordreset/<uid>/<token>/', UserPasswordResetView.as_view(), name='passwordreset'),
    
    
    
    
]