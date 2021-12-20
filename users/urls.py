from django.urls import path

from .views import CustomUserViewSet, PingGoogle

# router = DefaultRouter()
# router.register('users', CustomUserViewSet)

urlpatterns = [
    path(
        'latency/',
        PingGoogle.as_view(),
        name='goggle-latency',
    ),
    path(
        'info/',
        CustomUserViewSet.as_view({'get': 'me'}),
        name='info',
    ),
    path(
        'signup/',
        CustomUserViewSet.as_view({'post': 'create'}),
        name='signup',
    ),
]
