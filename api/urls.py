from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CommentViewSet, FollowListView, GroupListView, PostViewSet

router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<id>\d+)/comments',
                CommentViewSet, basename='Comment')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/group/', GroupListView.as_view()),
    path('v1/follow/', FollowListView.as_view()),
]
