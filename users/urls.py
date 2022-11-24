from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from courses import views
from courses.views import CoursesAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/courses', CoursesAPIView.as_view(), name = 'courses'),
]