from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import (
    UserListCreateAPI, 
    UserRetriveUpdateDeleteAPI
)


urlpatterns = [
    path('user/', UserListCreateAPI.as_view(), name='user'),
    path('user/<int:pk>/', UserRetriveUpdateDeleteAPI.as_view(), name='user-detail'),

    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
