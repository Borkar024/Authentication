from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app1.views import EmpViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('emp', EmpViewSet, basename='emp') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('auth/', include('auth_app.urls')),
    path('token/',obtain_auth_token),
]
