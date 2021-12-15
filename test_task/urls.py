from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenViewBase)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('logout/', TokenViewBase.as_view(), name='token_destoy'),
    path('signin/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('users.urls')),
]
