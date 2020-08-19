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
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('group/', GroupListView.as_view()),
    path('follow/', FollowListView.as_view()),
]
