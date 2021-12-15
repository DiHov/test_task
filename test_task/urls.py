from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^signin/', obtain_jwt_token),
    url(r'^signin/refresh/', refresh_jwt_token),
    path('', include('users.urls')),
]
