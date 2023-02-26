from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from user.views import (
    UserListCreateAPI, 
    UserRetriveUpdateDeleteAPI,
    TokenObtainPairView,
)


urlpatterns = [
    path('user/', UserListCreateAPI.as_view(), name='user'),
    path('user/<int:pk>/', UserRetriveUpdateDeleteAPI.as_view(), name='user-detail'),

    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]


# "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
# "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
# "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
# "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
# "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
# "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",