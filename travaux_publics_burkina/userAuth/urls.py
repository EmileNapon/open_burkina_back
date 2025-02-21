from django.urls import path
from .views import CustomTokenObtainPairView, RegisterView, UserDetailView, list_users

urlpatterns = [
    path('plateforme-integre/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('plateforme-integre/register/', RegisterView.as_view(), name='register_user'),
    path('plateforme-integre/user/', UserDetailView.as_view(), name='user_detail'),
    path('plateforme-integre/users/', list_users, name='list_users'),
]
